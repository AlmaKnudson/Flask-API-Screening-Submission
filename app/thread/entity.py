import jsonschema
from flask import current_app
from jsonschema import validate

# Could beef up the schema validation using definitions here (https://json-schema.org/learn/miscellaneous-examples.html)
threadSchema = {
    "type": "object",
    "properties": {
        "users": {
            "type": "array",
            "minItems": 2,
            "maxItems": 100,
            "items": {
                "type": "string"
            }
        }
    },
    "required": ["users"]
}

class ThreadEntity:
    @staticmethod
    def validate_json(json_data) -> bool:
        is_valid = False
        try:
            validate(instance=json_data, schema=threadSchema)
            is_valid = True
        except jsonschema.exceptions.ValidationError as err:
            current_app.logger.error('jsonschema ValidationError: %s', err.message)
            is_valid = False
        finally:
            return is_valid
