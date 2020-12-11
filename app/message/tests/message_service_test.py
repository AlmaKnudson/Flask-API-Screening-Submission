from app.message.service import MessageService


def test_valid_new_message(create_test_thread):
    for user in create_test_thread[1]:  # users
        mock_message_json = {
            "message": f'This is a message from {user}'
        }
        thread_id = MessageService.create_message(mock_message_json, create_test_thread[0], user)
        assert thread_id


def test_new_message_with_invalid_id():
    mock_message_json = {
        "message": "This is a message!"
    }
    thread_id = MessageService.create_message(mock_message_json, 'not_an_id', 'Kyle')
    assert not thread_id


def test_new_message_missing_message(create_test_thread):
    mock_message_json = {
        "taco": "This is not a message..."
    }
    thread_id = MessageService.create_message(mock_message_json, create_test_thread, 'Kyle')
    assert not thread_id
