import sqlite3

# Connect to database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Query to get all columns ordered by year
cursor.execute("SELECT * FROM books ORDER BY year")

# Print results
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
