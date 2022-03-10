import os
import functools
import flask
from http import HTTPStatus

def authorized(headers: dict) -> bool:
    if not headers:
        return False
    authorization = headers['Authorization']
    secret_key = os.environ.get('SECRET_KEY')
    if secret_key == authorization:
        return True
    return False
    

def auth_guard(f):
  @functools.wraps(f)
  def decorated_function(*args, **kwargs):
    # Do something with your request here
    headers = flask.request.headers
    if not authorized(headers):
      flask.abort(HTTPStatus.BAD_REQUEST)
    return f(*args, **kwargs)
  return decorated_function
