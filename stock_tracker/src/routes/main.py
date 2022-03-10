from flask import Blueprint
from http import HTTPStatus
from flask import Response
from stock_tracker.src.decorators.auth_guard import auth_guard

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
@auth_guard
def index():
    return Response(status=HTTPStatus.OK)
