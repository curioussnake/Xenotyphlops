import sys
from pathlib import Path
print(Path(__file__).parent.parent)
sys.path.append(str(Path(__file__).parent.parent))

from flask_service.app import main_service
from flask_service.app.in_mem_db.data_base import in_memory_db_users

if __name__ == '__main__':
    print([x.json() for x in in_memory_db_users])
    main_service.run(port=8080)
