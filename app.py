from flask import Flask, flash, redirect, render_template, request, session, url_for, abort, g, Response, make_response, jsonify
from flask_session import Session
import json
import configparser

# Resource: https://tedboy.github.io/flask/generated/werkzeug.generate_password_hash.html
from werkzeug.security import generate_password_hash, check_password_hash

from aagSQLmanager import aagSQLmanager

from helper import loginRequired, loggedInNotAllowed, APP_DATE_FORMAT, checkAllowance, renderEditorData


## !! It seems it's not needed to clean data from user inputs as mariadb uses prepared statements.

app = Flask(__name__)

# Setting some variables to be used in jinja templates.
app.jinja_env.globals['wiki_version'] = '9.0.0'
app.jinja_env.globals['project_status'] = 'development'


# RELOAD APP WHEN TEMPLATE CHANGES
app.config["TEMPLATES_AUTO_RELOAD"] = True  

# UTF-8 in JSON Responses.
app.config['JSON_AS_ASCII'] = False

# Configure session to use filesystem (instead of signed cookies) as per pset9. Still trying to understand how it works
# Why SESSION_PERMANENT = False if I can set a lifetime for a permanent session?

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Setup DB

def configure_db():
    if app.jinja_env.globals['project_status'] == 'development':
        db_config = {
            'user':'root',
            'password':'root',
            'host':'127.0.0.1',
            'port':3306,
            'database':'roseonwiki'
        }
    else:
        cfg = configparser.ConfigParser()
        cfg.read('db.ini')
        db_config = {
            'user': cfg['DATABASE']['user'],
            'password':cfg['DATABASE']['password'],
            'host':cfg['DATABASE']['host'],
            'port':int(cfg['DATABASE']['port']),
            'database':cfg['DATABASE']['database']
        }
    return db_config

dbconfig = configure_db()

def get_db():
    if not ('db' in g):
        g.db = aagSQLmanager(**dbconfig)
    
    return g.db

@app.before_first_request
def init_stuff():
    global PAGE_TYPES
    loc_db = aagSQLmanager(**dbconfig)

    PAGE_TYPES = dict()
    page_types_response = loc_db.execute('SELECT * FROM page_types')
    for pagetype in page_types_response:
        PAGE_TYPES[pagetype['name']] = pagetype['id']
    print(PAGE_TYPES)

    loc_db.close()


@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()



@app.before_request
def before_request_callback():
    #This ensure that I get a fresh connection for every request.
    get_db()

# Taken from pset 9 to ensure responses aren't cached
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Profile Routes

@app.route('/profile/<string:username>')
@loginRequired
def profile(username):
    db_res = g.db.execute('SELECT username,created FROM accounts WHERE username = ?', username.lower())
    if db_res == False:
        return redirect('error')
    elif len(db_res) == 0:
        return abort(404)
    else:
        return render_template('profile.html', user_info=db_res[0])

# Pages Routes

@app.route('/nova_pagina', methods=['GET', 'POST'])
@loginRequired
@checkAllowance(3)
def nova_pagina():
    db_res = g.db.execute("SELECT * FROM page_types")
    allowed_pages_relation = {d['name']:d['id'] for d in db_res}
    planets = g.db.execute("SELECT * FROM planets")
    return render_template('nova_pagina.html', page_types=db_res, allowed_pages_relation=allowed_pages_relation, planets=planets)

@app.route('/guia/<int:guia_id>')

def mostra_guia(guia_id):
    if not guia_id:
        flash('Guia n??o encontrado!')
        return redirect('/')
    else:
        guia_db = g.db.execute('SELECT * FROM content WHERE id = ?', guia_id)
        if guia_db != False and len(guia_db) == 1:
            page_content = g.db.execute('SELECT * FROM pages where content_id = ?', guia_id)
            if page_content != False:
                page_content = page_content[0]
                guide_content = renderEditorData(page_content['content'])
                return render_template('guia.html', guide_name = guia_db[0]['name'], guide_content=guide_content)
        else:
            flash('Algo deu errado!')
            return redirect('/')

# Authentication Routes

@app.route('/registrar', methods=['GET', 'POST'])
@loggedInNotAllowed
def registrar():
    if request.method == 'POST':
        if not request.form.get('username'):
            flash('Voc?? n??o inseriu um nome de usu??rio.')
            return render_template('register.html', category='error')
        elif not request.form.get('password'):
            flash('Voc?? n??o inseriu uma senha.')
            return render_template('register.html', category='error')
        elif not request.form.get('confirmation'):
            flash('Voc?? n??o inseriu uma confirma????o de senha.')
            return render_template('register.html', category='error')
        elif not (request.form.get('confirmation') == request.form.get('password')):
            flash('A senha e a confirma????o n??o s??o iguais.', category='error')
            return render_template('register.html')
        else:
            sent_username = request.form.get('username').lower()
            db_usrs = g.db.execute('SELECT username FROM accounts WHERE username = ?', sent_username)
            if db_usrs == False or len(db_usrs) > 0:
                flash('Este usu??rio j?? existe.', category='error')
                return redirect('/registrar')
            else:
                hash_password = generate_password_hash(request.form.get('password'))
                db_res = g.db.execute("INSERT INTO accounts(username, password) VALUES(?,?)", sent_username, hash_password)
                if db_res != False:
                    flash('Conta criada com sucesso!', category='success')
                else:
                    flash('Algo deu errado na cria????o de conta.', category='error')
                return redirect('/')
            
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
@loggedInNotAllowed
def login():
    if request.method == 'POST':
        if not request.form.get('username'):
            flash('Voc?? n??o inseriu um nome de usu??rio.', category='error')
            return redirect('/login')
        elif not request.form.get('password'):
            flash('Voc?? n??o inseriu uma senha', category='error')
            return redirect('/login')
        else:
            db_res = g.db.execute('SELECT * FROM accounts WHERE username = ?', request.form.get('username').lower())
            if db_res == False or len(db_res) > 1:
                flash('Algo deu errado!', category='error')
                return redirect('/login')
            elif len(db_res) == 0:
                flash('Este usu??rio n??o est?? cadastrado.', category='error')
                return redirect('/login')
            else:
                password = db_res[0]['password']
                if not check_password_hash(password, request.form.get('password')):
                    flash('Senha incorreta.', category='error')
                    return redirect('/login')
                else:
                    session['user_id'] = db_res[0]['id']
                    session['user_info'] = {'username':db_res[0]['username'], 'created_at':db_res[0]['created'].strftime(APP_DATE_FORMAT), 'allowance':db_res[0]['allowance']}
                    flash('Login com sucesso!', category='success')
                    return redirect('/profile/'+session['user_info']['username'])

    else:
        return render_template('login.html')

@app.route("/logout")
@loginRequired
def logout():
    session.clear()
    flash('Logout com sucesso!', category='success')
    return redirect("/")




# Handlers
@app.route('/error')
def errorGeneral():
    return render_template('error.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403

# API Routes

@app.route('/fetchUrl')
def fetch_url():
    return json.dumps({'success' : 1, 'link':request.args.get('url'), "meta":{}}), 200, {'ContentType':'application/json'}

@app.route('/api/getItemTypes')
@checkAllowance(3)
def get_item_types():
    return g.db.execute('SELECT * FROM item_types') 

@app.route('/api/getItemSubtypes')
@checkAllowance(3)
def get_item_subtypes():
    if not request.args.get('item_type'):
        return {}
    else:
        return g.db.execute('SELECT * FROM item_subtype WHERE item_type_id = ?', request.args.get('item_type')) 

@app.route('/api/getStatusTypes')
@checkAllowance(3)
def get_status_types():
    return g.db.execute('SELECT * FROM status_types')

@app.route('/api/getFieldsItemType')
@checkAllowance(3)
def get_fields_item_type():
    if not request.args.get('id'):
        return {}
    else:
        db_response = g.db.execute('SELECT * FROM item_types WHERE id = ?', request.args.get('id'))
        db_status = g.db.execute('SELECT * FROM status_types')
        
        if len(db_response) == 0 or len(db_response) > 1:
            return {}
        elif db_response[0]['name'] == 'arma':
            return {'fields':[
                {'type':'input', 'required':True, 'name':'weapon_attack_power', 'placeholder':'Poder de Ataque'},
                {'type':'input', 'required':True, 'name':'weapon_precision', 'placeholder':'Precis??o'},
                {'type':'input', 'required':True, 'name':'weapon_attack_speed', 'placeholder':'Velocidade de Ataque'},
                {'type':'input', 'required':True, 'name':'weapon_attack_range', 'placeholder':'Dist??ncia de Ataque'},
                {'type':'select', 'required':False, 'options':db_status, 'name':'weapon_status1_type', 'placeholder':'Selecione um Tipo de Status'},
                {'type':'input', 'required':False, 'name':'weapon_status1_value', 'placeholder':'Valor do Status'},
                {'type':'select', 'required':False, 'options':db_status, 'name':'weapon_status2_type', 'placeholder':'Selecione um Tipo de Status'},
                {'type':'input', 'required':False, 'name':'weapon_status2_value', 'placeholder':'Valor do Status'},
                {'type':'select', 'required':False, 'options':db_status, 'name':'weapon_status3_type', 'placeholder':'Selecione um Tipo de Status'},
                {'type':'input', 'required':False, 'name':'weapon_status3_value', 'placeholder':'Valor do Status'}
            ]}
        else:
            return {}

@app.route('/api/insertItem', methods=['POST'])
@checkAllowance(3)
def insert_item():
    return Response({'status':403, 'message':'Not yet available'}, 'Not yet available', 403)

@app.route('/api/insertGuide', methods=['POST'])
@checkAllowance(3)
def insert_guide():
    if not request.is_json:
        return Response('Invalid JSON Payload', 400)
    else:
        if not request.json.get('title'):
            return make_response({'status':400, 'message':'Missing Title'}, 400, {'Content-Type':'application/json'})
        elif not request.json.get('blocks'):
            return make_response({'status':400, 'message':'Missing Blocks'}, 400, {'Content-Type':'application/json'})
        else:
            content_id = g.db.execute('INSERT INTO content(name, type) VALUES(?,?)', request.json.get('title'), PAGE_TYPES['guia'])
            if content_id != False and content_id != None:
                page_response = g.db.execute('INSERT INTO pages(created_by, page_type, content_id, content) VALUES(?, ?, ?, ?)', session['user_id'], PAGE_TYPES['guia'], content_id, str(request.json.get('blocks')))
                if page_response != False:
                    page_response = g.db.execute('INSERT INTO guides(id, subject) VALUES(?,?)', content_id, request.json.get('title'))
                    return make_response({'status':200, 'message':'success!'}, 200, {'Content-Type':'application/json'})
                return make_response({'status':500, 'message':'Something wen\'t wrong in DB Operations'}, 500, {'Content-Type':'application/json'}) 
            else:
                return make_response({'status':500, 'message':'Something wen\'t wrong in DB Operations'}, 500, {'Content-Type':'application/json'})

