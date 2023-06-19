from typing import Dict, Any


class User:
    def __init__(self, name: str, lastname: str, role: str = "NONE"):
        self.id = f"{name[0]}{lastname}".lower()
        self.name = name
        self.lastname = lastname
        self.role = role

    def json(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "role": self.role,
        }

    def xml(self) -> str:
        return (
            "<user>"
            f"<id>{self.id}</id>"
            f"<name>{self.name}</name>"
            f"<lastname>{self.lastname}</lastname>"
            f"<role>{self.role}</role>"
            "</user>"
        )
