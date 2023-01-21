from flask import redirect, render_template, request, session, abort
from functools import wraps
import ast

import datetime

APP_DATE_FORMAT  = '%d/%m/%Y'

def loginRequired(route):
    """ Verify if user is logged-in for pages where it is required. """
    @wraps(route)
    def decorated_route(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect('/login')
        return route(*args, **kwargs)
    return decorated_route

def loggedInNotAllowed(route):
    """ Verify if a logged user is trying to access a page for not logged in users. """
    @wraps(route)
    def decorated_route(*args, **kwargs):
        if not(session.get('user_id') is None):
            return redirect('/')
        return route(*args, **kwargs)
    return decorated_route

def checkAllowance(allowance):
    """Verify if user has the allowance level for the selected page"""
    def innerDecor(route):
        @wraps(route)
        def decorated_route(*args, **kwargs):
            if session.get('user_info'):
                if session['user_info']['allowance'] >= allowance:
                    return route(*args, **kwargs)
                else:
                    return abort(403)
            else:
                return abort(403)
        return decorated_route
    return innerDecor

def renderEditorData(editor_data):
    WARNING_SYMBOL = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16"><path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575ZM8 5a.75.75 0 0 0-.75.75v2.5a.75.75 0 0 0 1.5 0v-2.5A.75.75 0 0 0 8 5Zm1 6a1 1 0 1 0-2 0 1 1 0 0 0 2 0Z"></path></svg>'
    editor_data = ast.literal_eval(editor_data)
    rendered_html = ''
    for item in editor_data:
        new_html = ''
        if not rendered_html == '':
            rendered_html = rendered_html + '\n'
        if item['type'] == 'paragraph':
            new_html = '<p>'+item['data']['text']+'</p>'
            
        elif item['type'] == 'list':
            
            if item['data']['style'] == 'unordered':
                new_html = '<br> <ul class="list-inside list-disc">'
                for li in item['data']['items']:
                    print('li:' + li)
                    new_html = new_html + '<li> '+ li + '</li>'
                new_html = new_html + '</ul><br>'
            elif item['data']['style'] == 'ordered':
                new_html = '<br> <ol class="list-inside">'
                for li in item['data']['items']:
                    print('li:' + li)
                    new_html = new_html + '<li> '+ li + '</li>'
                new_html = new_html + '</ul><br>'
        
        elif item['type'] == 'header':
            classes = {
                1:"font-inputs text-3xl text-center my-3 font-extrabold",
                2:"font-inputs text-2xl text-center my-3 font-bold",
                3:"font-inputs text-xl text-center my-3 font-medium",
                4:"font-inputs text-lg text-center my-3 font-medium",
                5:"font-inputs text-lg text-center my-3 font-medium",
                6:"font-inputs text-lg text-center my-3 font-medium"
            }
            new_html = '<h'+ str(item['data']['level'])+' class="' + classes[item['data']['level']] + '">' + item['data']['text'] + '</h'+str(item['data']['level'])+'>'
        elif item['type'] == 'quote':
            new_html = '<div class="bg-icewhite block font-opensans items-center bg-opacity-70 rounded p-6 my-3 "><span class="text-3xl block">"</span><div class="px-6 text-sm italic"><p class="text-justify leading-4">'+item['data']['text']+'</p></div><span class="text-3xl text-right block">"</span><div class="text-center"><span class="p-3 text-xs font-opensans font-bold bg-icewhite rounded-full"> — '+item['data']['caption']+'</span></div></div>'
        elif item['type'] == 'warning':
            new_html = '<div class="p-3 my-3  font-inputs bg-opacity-70 rounded-lg bg-yellowwarning">cc<span class="text-base text-center mb-3 font-inputs font-medium block">'+item['data']['title']+'</span><hr><div class="mt-3 flex items-center"><span class="inline-block">'+WARNING_SYMBOL+'</span><span class="mx-auto text-sm">'+item['data']['message']+'</span></div></div>'
        elif item['type'] == 'image':
            new_html = '<div class="p-3 my-3 text-center"><img class="rounded-xl mb-4 mx-auto" src="'+item['data']['url']+'"><span class="p-2 mt-3 text-xs font-opensans italic bg-icewhite rounded-full">'+item['data']['caption']+'</span></div>'
        elif item['type'] == 'linkTool':
            pass
        rendered_html = rendered_html + new_html

    


    return rendered_html