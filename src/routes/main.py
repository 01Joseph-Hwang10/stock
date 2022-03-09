from flask import Blueprint
from http import HTTPStatus
from flask import Response

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    return Response(status=HTTPStatus.OK)
