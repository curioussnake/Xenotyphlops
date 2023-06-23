from typing import Dict, Any


class Role:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def json(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
        }

    def xml(self) -> str:
        return (
            "<role>"
            f"<name>{self.name}</name>"
            f"<description>{self.description}</description>"
            "</role>"
        )
