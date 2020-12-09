from flask import request, Blueprint, current_app
import json

from app.message.service import MessageService

message_thread = Blueprint('message', __name__)


@message_thread.route('<thread_id>/<username>', methods=['POST'])
def create_message(thread_id, username):
    json_data = json.loads(request.data)
    current_app.logger.info(
        'Create_message called with payload: %s. And path parameters thread_id: %s, username: %s',
        json_data,
        thread_id,
        username
    )
    # Consider creating a consolidated/central error handling strategy to handle malformed requests, db connection
    # failure, etc...
    thread_id = MessageService.create_message(json_data, thread_id, username)

    if thread_id is None:  # The variable
        current_app.logger.debug('Create_thread failed to create thread.')
        return {'error': 'malformed request', 'data': json_data}, 400
    else:
        return {}, 204


# {
#     "messages": [
#         {"username": "jeff_goldblum", "message": "This is a message!"},
#         ...
#     ]
# }
@message_thread.route('<thread_id>', methods=['GET'])
def get_thread(thread_id):
    current_app.logger.info('Get_thread called for thread_id: %s', thread_id)
    thread_messages = MessageService.get_thread_messages(thread_id)
    return {"messages": thread_messages}, 200
