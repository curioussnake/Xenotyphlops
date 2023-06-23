from flask import Flask

main_service = Flask(__name__)

from flask_service.app.service import users
