from flask import request, Blueprint, current_app
import json

from app.thread.service import ThreadService

thread = Blueprint('thread', __name__)


@thread.route('', methods=['POST'])
def create_thread():
    json_data = json.loads(request.data)
    current_app.logger.info('Create_thread called with payload: %s', json_data)
    # Consider creating a consolidated/central error handling strategy to handle malformed requests, db connection
    # failure, etc...
    thread_id = ThreadService.create_thread(json_data)
    if thread_id is None:  # The variable
        current_app.logger.debug('Create_thread failed to create thread.')
        return {'error': 'malformed request', 'data': json_data}, 400
    else:
        data = {'thread_id': str(thread_id)}
        current_app.logger.debug('Create_thread returning: %s', data)
        return data, 201
