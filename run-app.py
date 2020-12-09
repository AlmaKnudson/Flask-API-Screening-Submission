# -*- coding: utf-8 -*-

from app import create_app
from dotenv import load_dotenv

load_dotenv()
from config import Config

if __name__ == '__main__':
    # Running app in debug mode
    app = create_app()
    app.run(debug=Config.DEBUG)
