import jsonschema
from flask import current_app
from jsonschema import validate

newMessageSchema = {
    "type": "object",
    "properties": {
        "message": {"type": "string", "minLength": 2, "maxLength": 280},  # Max message length is the same as a Tweet.
        "username": {"type": "string"},
        "thread_id": {"type": "string"}
    },
    "required": ["message", "username", "thread_id"]
}


class MessageEntity:
    @staticmethod
    def validate_json(json_data) -> bool:
        is_valid = False
        try:
            validate(instance=json_data, schema=newMessageSchema)
            is_valid = True
        except jsonschema.exceptions.ValidationError as err:
            current_app.logger.error('jsonschema ValidationError: %s', err.message)
            is_valid = False
        finally:
            return is_valid
