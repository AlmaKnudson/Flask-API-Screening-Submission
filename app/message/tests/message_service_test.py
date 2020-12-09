from app.message.service import MessageService


def test_valid_new_message(test_client):
    mock_message_json = {
        "message": "This is a message!"
    }
    thread_id = MessageService.create_message(mock_message_json, '123', 'Kyle')
    assert thread_id


def test_new_message_missing_message(test_client):
    mock_message_json = {
        "taco": "This is not a message..."
    }
    thread_id = MessageService.create_message(mock_message_json, '123', 'Kyle')
    assert not thread_id
