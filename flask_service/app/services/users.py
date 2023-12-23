from flask import request

from flask_service.app import main_service
from werkzeug.exceptions import abort
from flask_service.app.utils.user import User
from flask_service.app.utils.error_handling import bad_request_response
from flask_service.app.in_mem_db.data_base import in_memory_db_users, in_memory_db_roles


@main_service.route('/users', methods=["GET"])
def users():
    accept = request.headers.get("Accept")
    if accept == "application/xml":
        return f"<users>{''.join([x.xml() for x in in_memory_db_users])}</users>"
    return [x.json() for x in in_memory_db_users]


@main_service.route('/users/<user_id>', methods=["DELETE"])
def delete_user(user_id: str):
    user_to_delete = next((x for x in in_memory_db_users if x.id == user_id), None)

    if user_to_delete is not None:
        in_memory_db_users.remove(user_to_delete)
        accept = request.headers.get("Accept")
        if accept == "application/xml":
            return f"<users>{''.join([x.xml() for x in in_memory_db_users])}</users>"
        return [x.json() for x in in_memory_db_users]
    else:
        abort(404, description=f"User {user_id} not found!")

@main_service.route('/users/<user_id>', methods=["GET"])
def user_by_id(user_id: str):
    user = [x for x in in_memory_db_users if x.id == user_id]
    if len(user) == 1:
        accept = request.headers.get("Accept")
        if accept == "application/xml":
            return user[0].xml()
        return user[0].json()
    abort(404, description=f"User {user_id} not found!")


@main_service.route('/users', methods=["POST"])
def add_user():
    content_type = request.headers.get("content-type")
    if content_type == "application/json":
        if request.data == '':
            return bad_request_response(description="Lack of required data in body!")
        if "name" not in request.json.keys() or "lastname" not in request.json.keys():
            return bad_request_response(
                description=f"Lack of required data in body: {set(['name', 'lastname']) - set(request.json.keys())}!"
            )
        if "role" in request.json.keys():
            if request.json["role"] not in in_memory_db_roles.keys():
                return bad_request_response(
                    description=f"Role: {request.json['role']} not allowed!"
                )
        new_user = User(
            name=request.json["name"],
            lastname=request.json["lastname"],
            role=request.json["role"] if "role" in request.json.keys() else "NONE"
        )
        in_memory_db_users.append(new_user)
        accept = request.headers.get("Accept")
        if accept == "application/xml":
            return new_user.xml(), 201
        return new_user.json(), 201
    abort(
        status=422,
        description=f"Incorrect content type: {content_type}!"
    )


@main_service.route('/users/<user_id>', methods=["PUT"])
def update_user(user_id: str):
    user = [x for x in in_memory_db_users if x.id == user_id]
    if len(user) != 1:
        abort(404, description=f"User {user_id} not found!")
    content_type = request.headers.get("content-type")
    if content_type == "application/json":
        if request.data == '':
            return bad_request_response(description="Lack of required data in body!")
        if "name" not in request.json.keys() or "lastname" not in request.json.keys():
            return bad_request_response(
                description=f"Lack of required data in body: {set(['name', 'lastname']) - set(request.json.keys())}!"
            )
        if "role" in request.json.keys():
            if request.json["role"] not in in_memory_db_roles.keys():
                return bad_request_response(
                    description=f"Role: {request.json['role']} not allowed!"
                )
        user_to_update = user[0]
        user_to_update.name = request.json["name"]
        user_to_update.lastname = request.json["lastname"]
        user_to_update.role = request.json["role"] if "role" in request.json.keys() else "NONE"
        accept = request.headers.get("Accept")
        if accept == "application/xml":
            return user_to_update.xml(), 200
        return user_to_update.json(), 200
    abort(
        status=422,
        description=f"Incorrect content type: {content_type}!"
    )
