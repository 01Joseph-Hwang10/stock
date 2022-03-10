import json
from flask import Blueprint
from http import HTTPStatus
from flask import Response
from shared.hooks.use_config import use_config
from shared.utils.time import now

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    response = {
        'is_healthy': True,
        'has_config': bool(use_config()),
        'current_time': now(True),
    }
    return Response(status=HTTPStatus.OK, response=json.dumps(response))
