import csv

# Open and read books.csv
with open("/Users/ckiefer/projects/220 - Python/Module 4/CashKiefer-SDEV220-M04A1c/books.csv", newline='', encoding="utf-8") as csvfile:
    books = csv.DictReader(csvfile)  # Read CSV as a dictionary

    # Print each row
    for row in books:
        print(row)
