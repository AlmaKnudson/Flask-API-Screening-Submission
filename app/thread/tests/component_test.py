import json

from app import create_app


def test_base_route():
    flask_app = create_app()
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
    with flask_app.test_client() as test_client:
        response = test_client.post('/thread', data=json.dumps(mock_request_data), headers=mock_request_headers)
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['thread_id']




