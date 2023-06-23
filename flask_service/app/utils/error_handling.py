import json

from flask_service.app import main_service
from flask import Response


def bad_request_response(description: str) -> Response:
    print("Own error handling 400!")
    print(f"handle_bad_request: {description}")
    return Response(
        response=json.dumps(
            {
                "error": "Bad request",
                "message": description
            }
        ),
        status=400
    )


@main_service.errorhandler(404)
def handle_user_not_found(e):
    print("Own error handling 404!")
    print(f"handle_bad_request: {e.description}")
    print(f"e: {str(e)}")
    return json.dumps(
        {
            "error": "Not Found",
            "message": e.description
        }
    ), 404


@main_service.errorhandler(422)
def handle_unprocessable_entity(e):
    print("Own error handling 422!")
    print(f"handle_bad_request: {e.description}")
    print(f"e: {str(e)}")
    return json.dumps(
        {
            "error": "Not Found",
            "message": e.description
        }
    ), 422