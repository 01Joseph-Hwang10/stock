import json
from flask import Blueprint
from http import HTTPStatus
from flask import Response
from flask import request
from stock_tracker.src.decorators.auth_guard import auth_guard
from shared.hooks.use_config import use_config
from shared.hooks.use_config import config_path

bp = Blueprint('config', __name__, url_prefix='/config')

"""
Request Method : POST
Request Body : {
    config: Config,
}
"""
@bp.route('/upload', methods=['POST'])
@auth_guard
def upload_config():
    try:
        config = request.get_json()['config']
        with open(config_path, 'w') as f:
            f.write(json.dumps(config, indent=2))
        return Response(status=HTTPStatus.OK)
    except:
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
