import sqlite3

conn = sqlite3.connect(my_database.db)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER NOT NULL PRIMARY KEY,
        name TEXT,
        lastname TEXT,
        role INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS roles (
        id INTEGER NOT NULL PRIMARY KEY,
        name TEXT,
        description TEXT
    )
''')

conn.commit()
conn.close()