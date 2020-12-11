import json

from app import create_app

mock_request_headers = {
    "Content-Type": "application/json"
}


def test_create_message(create_test_thread):
    flask_app = create_app()
    # thread_id = create_thread()
    mock_request_data = {
        "message": "This is a message!"
    }

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post(f'/thread/{create_test_thread[0]}/{create_test_thread[1][0]}', data=json.dumps(mock_request_data),
                                    headers=mock_request_headers)
        assert response.status_code == 204


def test_get_thread(create_test_thread):
    flask_app = create_app()
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get(f'/thread/{create_test_thread[0]}', headers=mock_request_headers)
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['messages']
        assert len(response_data['messages']) > 0
