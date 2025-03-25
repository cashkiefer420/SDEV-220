import csv
import sqlite3

# Connect to database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Open books2.csv and insert data into books table
with open("/Users/ckiefer/projects/220 - Python/Module 4/CashKiefer-SDEV220-M04A1c/books2.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
                       (row['title'], row['author'], int(row['year'])))

# Commit and close
conn.commit()
conn.close()
