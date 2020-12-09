

def test_valid_new_message(message_entity):
    """
    GIVEN a new valid message json
    WHEN a new message is validated
    THEN assert is valid
    """

    mock_message_json = {
        "message": "This is a message!",
        "thread_id": "123",
        "username": "bob"
    }
    is_valid = message_entity.validate_json(mock_message_json)
    assert is_valid


def test_valid_new_message_with_random_additional_information(message_entity):
    mock_message_json = {
        "message": "This is a message!",
        "thread_id": "123",
        "username": "bob",
        "taco": "shell"
    }
    is_valid = message_entity.validate_json(mock_message_json)
    assert is_valid

def test_new_message_missing_thread_id(message_entity):
    mock_message_json = {
        "message": "This is a message!",
        "username": "bob",
        "taco": "shell"
    }
    is_valid = message_entity.validate_json(mock_message_json)
    assert not is_valid

def test_new_message_missing_message(message_entity):
        mock_message_json = {
            "thread_id": "5fd10a9f0fcb41725938980e",
            "username": "bob"
        }
        is_valid = message_entity.validate_json(mock_message_json)
        assert not is_valid


def test_new_message_missing_username(message_entity):
    mock_message_json = {
        "thread_id": "5fd10a9f0fcb41725938980e",
        "message": "Some Message"
    }
    is_valid = message_entity.validate_json(mock_message_json)
    assert not is_valid

def test_new_message_longer_than_280_characters(message_entity):
    mock_message_json = {
        "message": "718bbVXFqJyOeewMiNHzjeuKWY3R8vbTOcOwS17c4uluTM1B4K3gF4vHCLCI8T"
                   "8cQuNN5ZwJ5QKM4urXcYoHPn53wyobPytzKdp697GUQP0rcwWk0mdha4gnZ5AWEI"
                   "8wUdXHjibbHyj8mahgEkB1B3KFz19j71f9odBntSxxnsrHxYUYWmiP94NmABT3n9"
                   "ue0ycRt99BXgyYWgznfSfQNjGcXBImqSwpqyYJ2gHESh8q2VCPu6mzCy4aXmF9DJ08DMuA1dUMLRQvKJ2cEprF8NrE",
        "thread_id": "123",
        "username": "bob"
    }
    is_valid = message_entity.validate_json(mock_message_json)
    assert is_valid

def test_new_message_longer_than_280_characters(message_entity):
    mock_message_json = {
        "message": "1718bbVXFqJyOeewMiNHzjeuKWY3R8vbTOcOwS17c4uluTM1B4K3gF4vHCLCI8T"
                   "8cQuNN5ZwJ5QKM4urXcYoHPn53wyobPytzKdp697GUQP0rcwWk0mdha4gnZ5AWEI"
                   "8wUdXHjibbHyj8mahgEkB1B3KFz19j71f9odBntSxxnsrHxYUYWmiP94NmABT3n9"
                   "ue0ycRt99BXgyYWgznfSfQNjGcXBImqSwpqyYJ2gHESh8q2VCPu6mzCy4aXmF9DJ08DMuA1dUMLRQvKJ2cEprF8NrE",
        "thread_id": "123",
        "username": "bob"
    }
    is_valid = message_entity.validate_json(mock_message_json)
    assert not is_valid