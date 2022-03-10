from flask import Blueprint
from http import HTTPStatus
from flask import Response

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return Response(status=HTTPStatus.OK)
