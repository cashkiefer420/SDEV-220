import sqlite3

# Connect to (or create) books.db
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Create books table
cursor.execute('''
    CREATE TABLE books (
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

# Commit and close
conn.commit()
conn.close()
