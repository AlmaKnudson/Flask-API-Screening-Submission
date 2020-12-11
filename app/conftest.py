import json

import pytest

from app import create_app
from app.message.entity import MessageEntity


@pytest.fixture(scope='module')
def message_entity():
    return MessageEntity


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    # Establish an application context before running the tests.

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def create_test_thread(test_client):
    mock_request_headers = {
        "Content-Type": "application/json"
    }

    mock_request_data = {
        "users": [
            "quinn",
            "jeff_goldblum"
        ]
    }

    # Create a test client using the Flask application configured for testing
    response = test_client.post('/thread', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 201
    data = json.loads(response.data)
    yield data['thread_id'], mock_request_data["users"]
