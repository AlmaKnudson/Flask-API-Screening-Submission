from app.thread.service import ThreadService

def test_valid_new_message(test_client):
    mock_thread_json = {
        "users": [
            "quinn",
            "jeff_goldblum"
        ]
    }
    thread_id = ThreadService.create_thread(mock_thread_json)
    assert thread_id


def test_new_message_missing_users(test_client):
    mock_thread_json = {
        "userss": [
            "quinn",
            "jeff_goldblum"
        ]
    }
    thread_id = ThreadService.create_thread(mock_thread_json)
    assert not thread_id


def test_new_message_empty_users(test_client):
    mock_thread_json = {
        "users": []
    }
    thread_id = ThreadService.create_thread(mock_thread_json)
    assert not thread_id

def test_new_message_one_user(test_client):
    mock_thread_json = {
        "users": ["User1"]
    }
    thread_id = ThreadService.create_thread(mock_thread_json)
    assert not thread_id

def test_new_message_max_users(test_client):
    a_list = list(range(0, 100))
    max_number_of_users = [f'User{str(entry)}' for entry in a_list]
    mock_thread_json = {
        "users": max_number_of_users
    }
    thread_id = ThreadService.create_thread(mock_thread_json)
    assert thread_id

def test_new_message_exceeding_max_users(test_client):
    a_list = list(range(0, 101))
    max_number_of_users = [f'User{str(entry)}' for entry in a_list]
    mock_thread_json = {
        "users": max_number_of_users
    }
    thread_id = ThreadService.create_thread(mock_thread_json)
    assert not thread_id