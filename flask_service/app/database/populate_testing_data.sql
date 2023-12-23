import sqlite3

conn = sqlite3.connect(my_database.db)

cursor = conn.cursor()

cursor.execute('''
    INSERT INTO USERS (user_id, user_name, user_lastname, user_role)
    VALUES ('Test','FirstTest','1'),
    ('John','Testowy','1')
''')

cursor.execute('''
    INSERT INTO ROLES (role_id, role_name, role_description)
    VALUES ('ADMIN','For administration purpose'),
    ('MODERATOR','To moderate content,'),
    ('VIEWER','Can only view content.'),
    ('NONE','No role assigned currently.')
''')

conn.commit()
conn.close()