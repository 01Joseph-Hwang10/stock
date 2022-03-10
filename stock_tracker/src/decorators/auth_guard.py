import os
import functools
import flask
from http import HTTPStatus

def authorized(data: dict) -> bool:
    if not data:
        return False
    authorization = data['headers']['Authorization']
    secret_key = os.environ.get('SECRET_KEY')
    if secret_key == authorization:
        return True
    return False
    

def auth_guard(f):
  @functools.wraps(f)
  def decorated_function(*args, **kwargs):
    # Do something with your request here
    data = flask.request.get_json()
    if not authorized(data):
      flask.abort(HTTPStatus.BAD_REQUEST)
    return f(*args, **kwargs)
  return decorated_function
