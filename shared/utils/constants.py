import os

ROOT = os.path.join(os.path.dirname(__file__), '..', '..')

STATIC = os.path.join(ROOT, 'static')

SERVER_URL = None

if os.environ.get('DEBUG') == 'True':
    SERVER_URL = 'http://localhost:5000'
else:
    SERVER_URL = 'http://stock-env.eba-hirrdtdm.ap-northeast-2.elasticbeanstalk.com/'
