from typing import Optional, Any

from bson import ObjectId
from bson.errors import InvalidId
from flask import current_app

from app.thread.entity import ThreadEntity

from config import Config

threadsTable = Config.DATABASE["threads"]


class ThreadService:
    @staticmethod
    def create_thread(json_data) -> Any:
        # this section of code is a candidate for refactoring/consolidation
        is_valid = ThreadEntity.validate_json(json_data)
        if is_valid:
            current_app.logger.debug('JSON IS VALID. Will save thread in DB.')
            result = threadsTable.insert_one(json_data)
            current_app.logger.debug("Inserted Id: %s" + str(result.inserted_id))
            return result.inserted_id
        else:
            current_app.logger.error("JSON WAS INVALID. Will... idk yet.")
            return None

    @staticmethod
    def get_thread_with_id_and_username(thread_id, username) -> Optional[Any]:
        try:
            return threadsTable.find_one({"_id": ObjectId(thread_id), "users": {"$elemMatch": {"$eq": username}}})
        except InvalidId as exception:
            current_app.logger.debug(f'Invalid id or username was used ({thread_id}, {username})')
            return None
