import json
from flask import Blueprint
from http import HTTPStatus
from flask import Response
from shared.hooks.use_config import use_config
from shared.utils.time import now
from stock_tracker.src.scheduler.main import scheduler
from shared.utils.metadata import LAST_UPDATED

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    job_status = {
        'notify': scheduler.status_of('notify')
    }
    response = {
        'is_healthy': True,
        'has_config': bool(use_config()),
        'current_time': now(True),
        'job_status': job_status,
        'last_updated': LAST_UPDATED,
    }
    return Response(status=HTTPStatus.OK, response=json.dumps(response))
