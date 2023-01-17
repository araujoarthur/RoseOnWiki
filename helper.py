from flask import redirect, render_template, request, session, abort
from functools import wraps

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