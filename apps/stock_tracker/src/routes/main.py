from flask import Blueprint
from http import HTTPStatus
from flask import Response
from apps.shared.decorators.auth_guard import auth_guard

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
@auth_guard
def index():
    return Response(status=HTTPStatus.OK)
