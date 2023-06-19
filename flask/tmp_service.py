import json

from flask import Flask, request, Response
from utils.user import User


app = Flask(__name__)

in_memory_db = [
    User(
        name="Test",
        lastname="FirstTest"
    ),
    User(
        name="John",
        lastname="Testowy"
    )
]


@app.route('/users', methods=["GET"])
def users():
    accept = request.headers.get("Accept")
    if accept == "application/xml":
        return f"<users>{''.join([x.xml() for x in in_memory_db])}</users>"
    return [x.json() for x in in_memory_db]


@app.route('/users/<user_id>', methods=["GET"])
def user_by_id(user_id: str):
    user = [x for x in in_memory_db if x.id == user_id]
    if len(user) == 1:
        accept = request.headers.get("Accept")
        if accept == "application/xml":
            return user[0].xml()
        return user[0].json()
    return Response(
        response=json.dumps(
            {
                "error": "Not Found",
                "message": f"User {user_id} not found!"
            }
        ),
        status=404
    )


@app.route('/users', methods=["post"])
def add_user():
    content_type = request.headers.get("content-type")
    if content_type == "application/json":
        if request.data == '':
            return Response(
                response=json.dumps(
                    {
                        "error": "Body problem",
                        "message": f"Lack of required data in body!"
                    }
                ),
                status=400
            )
        if "name" not in request.json.keys() or "lastname" not in request.json.keys():
            return Response(
                response=json.dumps(
                    {
                        "error": "Body problem",
                        "message": f"Lack of required data in body: {set(['name', 'lastname']) - set(request.json.keys())}!"
                    }
                ),
                status=400
            )
        new_user = User(
            name=request.json["name"],
            lastname=request.json["lastname"],
            role=request.json["role"] if "role" in request.json.keys() else "NONE"
        )
        in_memory_db.append(new_user)
        accept = request.headers.get("Accept")
        if accept == "application/xml":
            return new_user.xml(), 201
        return new_user.json(), 201
    return Response(
        response=json.dumps(
            {
                "error": "Body problem",
                "message": f"Incorrect content type: {content_type}!"
            }
        ),
        status=422
    )


@app.route('/users/<user_id>', methods=["put"])
def update_user(user_id: str):
    user = [x for x in in_memory_db if x.id == user_id]
    if len(user) != 1:
        return Response(
            response=json.dumps(
                {
                    "error": "Not Found",
                    "message": f"User {user_id} not found!"
                }
            ),
            status=404
        )
    content_type = request.headers.get("content-type")
    if content_type == "application/json":
        if request.data == '':
            return Response(
                response=json.dumps(
                    {
                        "error": "Body problem",
                        "message": f"Lack of required data in body!"
                    }
                ),
                status=400
            )
        if "name" not in request.json.keys() or "lastname" not in request.json.keys():
            return Response(
                response=json.dumps(
                    {
                        "error": "Body problem",
                        "message": f"Lack of required data in body: {set(['name', 'lastname']) - set(request.json.keys())}!"
                    }
                ),
                status=400
            )
        user_to_update = user[0]
        user_to_update.name = request.json["name"]
        user_to_update.lastname = request.json["lastname"]
        user_to_update.role = request.json["role"] if "role" in request.json.keys() else "NONE"
        accept = request.headers.get("Accept")
        if accept == "application/xml":
            return user_to_update.xml(), 201
        return user_to_update.json(), 201
    return Response(
        response=json.dumps(
            {
                "error": "Body problem",
                "message": f"Incorrect content type: {content_type}!"
            }
        ),
        status=422
    )


if __name__ == '__main__':
    print([x.json() for x in in_memory_db])
    app.run(port=8080)
