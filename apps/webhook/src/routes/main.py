from flask import Blueprint, Response
from http import HTTPStatus
from apps.shared.decorators.auth_guard import auth_guard

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
@auth_guard
def index():
    return Response(status=HTTPStatus.OK)
