import sqlite3

# Connect to database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Query to get book titles in alphabetical order
cursor.execute("SELECT title FROM books ORDER BY title")

# Print results
for row in cursor.fetchall():
    print(row[0])

# Close connection
conn.close()
