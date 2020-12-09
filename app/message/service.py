from flask import current_app

from app.message.entity import MessageEntity

from config import Config

messagesTable = Config.DATABASE["messages"]


class MessageService:
    @staticmethod
    def get_thread_messages(thread_id) -> [dict]:
        cursor = messagesTable.find({"thread_id": thread_id}, {"username": 1, "message": 1, "_id": 0})
        messages = []
        for message in cursor:
            messages.append(message)
        current_app.logger.debug('Found %s messages in thread: %s', len(messages), thread_id)
        return messages

    @staticmethod
    def create_message(json_data, thread_id, username) -> any:
        json_data['thread_id'] = thread_id
        json_data['username'] = username
        # this section of code is a candidate for refactoring/consolidation
        is_valid = MessageEntity.validate_json(json_data)
        if is_valid:
            current_app.logger.debug('JSON IS VALID. Will save thread in DB.')
            result = messagesTable.insert_one(json_data)
            current_app.logger.debug("Inserted Id: %s" + str(result.inserted_id))
            return result.inserted_id
        else:
            current_app.logger.error("JSON WAS INVALID. Will... idk yet.")
