from flask import request

from flask_service.app import main_service
from werkzeug.exceptions import abort
from flask_service.app.utils.user import User
from flask_service.app.utils.error_handling import bad_request_response
from flask_service.app.in_mem_db.data_base import in_memory_db_users, in_memory_db_roles


@main_service.route('/roles', methods=["GET"])
def get_roles():
    accept = request.headers.get("Accept")
    if accept == "application/xml":
        return f"<roles>{''.join([f'<role>{key}</role>' for key, value in in_memory_db_roles.items()])}</roles>"
    return [key for key, value in in_memory_db_roles.items()]


@main_service.route('/roles/<role_id>', methods=["GET"])
def role_by_id(role_id: str):
    if role_id.upper() in in_memory_db_roles.keys():
        accept = request.headers.get("Accept")
        if accept == "application/xml":
            return in_memory_db_roles[role_id.upper()].xml()
        return in_memory_db_roles[role_id.upper()].json()
    abort(404, description=f"Role {role_id} not found!")
