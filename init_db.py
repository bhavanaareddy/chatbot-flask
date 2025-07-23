import sqlite3

conn = sqlite3.connect("chat.db")  # This will create the DB file if not exists
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    bot TEXT NOT NULL
)
''')

conn.commit()
conn.close()
