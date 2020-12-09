import json

from app import create_app

mock_thread_id = "33333"
mock_request_headers = {
    "Content-Type": "application/json"
}
mock_username = "Some rando"

def test_create_message():
    flask_app = create_app()

    mock_request_data = {
        "message": "This is a message!"
    }

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post(f'/thread/{mock_thread_id}/{mock_username}', data=json.dumps(mock_request_data), headers=mock_request_headers)
        assert response.status_code == 204


def test_get_thread():
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get(f'/thread/{mock_thread_id}', headers=mock_request_headers)
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['messages']
        assert len(response_data['messages']) > 0


