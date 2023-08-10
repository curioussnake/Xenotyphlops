from typing import Dict, Any


class Validation:

    def set_header(self, header) -> Dict[str, Any]:
        return {"accept": header}