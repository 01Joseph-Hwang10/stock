import functools
import flask
from apps.shared.hooks.use_config import use_config

config = use_config()

def authorized(data: dict) -> bool:
    if not data:
        return False
    authorization = data['headers']['Authorization']
    if config['env']['secretKey'] == authorization:
        return True
    return False
    

def auth_guard(f):
  @functools.wraps(f)
  def decorated_function(*args, **kwargs):
    # Do something with your request here
    data = flask.request.get_json()
    if not authorized(data):
      flask.abort(400)
    return f(*args, **kwargs)
  return decorated_function
