from typing import Dict, Any


class Validation:

    def set_header(self, headers) -> Dict[str, Any]:
        return {"accept": headers}