from flask import Blueprint
from http import HTTPStatus
from flask import Response
from stock_tracker.src.decorators.auth_guard import auth_guard

bp = Blueprint('config', __name__, url_prefix='/config')

@bp.route('/upload', methods=['POST'])
@auth_guard
def config():
    return Response(status=HTTPStatus.OK)
