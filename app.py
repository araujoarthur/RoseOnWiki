from flask import Flask, flash, redirect, render_template, request, session, url_for, abort
from flask_session import Session
import json

# Resource: https://tedboy.github.io/flask/generated/werkzeug.generate_password_hash.html
from werkzeug.security import generate_password_hash, check_password_hash

from aagSQLmanager import aagSQLmanager

from helper import loginRequired, loggedInNotAllowed, APP_DATE_FORMAT, checkAllowance


## !! It seems it's not needed to clean data from user inputs as mariadb uses prepared statements.

app = Flask(__name__)

# Setting some variables to be used in jinja templates.
app.jinja_env.globals['wiki_version'] = '1.0.0'
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
dbconfig = {
    'user':'root',
    'password':'root',
    'host':'127.0.0.1',
    'port':3306,
    'database':'roseonwiki'
}
db = aagSQLmanager(**dbconfig)

# Taken from pset 9 to ensure responses aren't cached

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        if not session.get('user_id'):
            return render_template('index.html')
        else:
            return redirect('/profile/'+session['user_info']['username'])

# Profile Routes

@app.route('/profile/<string:username>')
@loginRequired
def profile(username):
    db_res = db.execute('SELECT username,created FROM accounts WHERE username = ?', username.lower())
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
    db_res = db.execute("SELECT * FROM page_types")
    allowed_pages_relation = {d['name']:d['id'] for d in db_res}
    planets = db.execute("SELECT * FROM planets")
    return render_template('nova_pagina.html', page_types=db_res, allowed_pages_relation=allowed_pages_relation, planets=planets)


# Authentication Routes

@app.route('/registrar', methods=['GET', 'POST'])
@loggedInNotAllowed
def registrar():
    if request.method == 'POST':
        if not request.form.get('username'):
            flash('Você não inseriu um nome de usuário.')
            return render_template('register.html', category='error')
        elif not request.form.get('password'):
            flash('Você não inseriu uma senha.')
            return render_template('register.html', category='error')
        elif not request.form.get('confirmation'):
            flash('Você não inseriu uma confirmação de senha.')
            return render_template('register.html', category='error')
        elif not (request.form.get('confirmation') == request.form.get('password')):
            flash('A senha e a confirmação não são iguais.', category='error')
            return render_template('register.html')
        else:
            sent_username = request.form.get('username').lower()
            db_usrs = db.execute('SELECT username FROM accounts WHERE username = ?', sent_username)
            if db_usrs == False or len(db_usrs) > 0:
                flash('Este usuário já existe.', category='error')
                return redirect('/registrar')
            else:
                hash_password = generate_password_hash(request.form.get('password'))
                db_res = db.execute("INSERT INTO accounts(username, password) VALUES(?,?)", sent_username, hash_password)
                if db_res != False:
                    flash('Conta criada com sucesso!', category='success')
                else:
                    flash('Algo deu errado na criação de conta.', category='error')
                return redirect('/')
            
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
@loggedInNotAllowed
def login():
    if request.method == 'POST':
        if not request.form.get('username'):
            flash('Você não inseriu um nome de usuário.', category='error')
            return redirect('/login')
        elif not request.form.get('password'):
            flash('Você não inseriu uma senha', category='error')
            return redirect('/login')
        else:
            db_res = db.execute('SELECT * FROM accounts WHERE username = ?', request.form.get('username').lower())
            if db_res == False or len(db_res) > 1:
                flash('Algo deu errado!', category='error')
                return redirect('/login')
            elif len(db_res) == 0:
                flash('Este usuário não está cadastrado.', category='error')
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
    return db.execute('SELECT * FROM item_types') 

@app.route('/api/getItemSubtypes')
@checkAllowance(3)
def get_item_subtypes():
    if not request.args.get('item_type'):
        return {}
    else:
        return db.execute('SELECT * FROM item_subtype WHERE item_type_id = ?', request.args.get('item_type')) 

@app.route('/api/getStatusTypes')
@checkAllowance(3)
def get_status_types():
    return db.execute('SELECT * FROM status_types')

@app.route('/api/getFieldsItemType')
@checkAllowance(3)
def get_fields_item_type():
    if not request.args.get('id'):
        return {}
    else:
        db_response = db.execute('SELECT * FROM item_types WHERE id = ?', request.args.get('id'))
        if len(db_response) == 0 or len(db_response) > 1:
            return {}
        elif db_response[0]['name'] == 'arma':
            return {'fields':[
                {'name':'weapon_attack_power', 'placeholder':'Poder de Ataque'},
                {'name':'weapon_precision', 'placeholder':'Precisão'},
                {'name':'weapon_attack_speed', 'placeholder':'Velocidade de Ataque'},
                {'name':'weapon_attack_range', 'placeholder':'Distância de Ataque'},
                {'name':'weapon_status1_type', 'placeholder':'Selecione um Tipo de Status'},
                {'name':'weapon_status1_value', 'placeholder':'Valor do Status'},
                {'name':'weapon_status2_type', 'placeholder':'Selecione um Tipo de Status'},
                {'name':'weapon_status2_value', 'placeholder':'Valor do Status'},
                {'name':'weapon_status3_type', 'placeholder':'Selecione um Tipo de Status'},
                {'name':'weapon_status3_value', 'placeholder':'Valor do Status'}
            ]}
        else:
            return {}