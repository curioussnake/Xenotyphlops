from flask_service.app.utils.user import User
from flask_service.app.utils.role import Role

in_memory_db_users = [
    User(
        name="Test",
        lastname="FirstTest"
    ),
    User(
        name="John",
        lastname="Testowy"
    )
]


in_memory_db_roles = {
    "NONE": Role(
        name="None",
        description="Cannot see any content."
    ),
    "VIEWER": Role(
        name="Viewer",
        description="For view content."
    ),
    "MODERATOR": Role(
        name="Moderator",
        description="For moderate content."
    ),
    "ADMIN": Role(
        name="Admin",
        description="For admit content and service."
    )
}
