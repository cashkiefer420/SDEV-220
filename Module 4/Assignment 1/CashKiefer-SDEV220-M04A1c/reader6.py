from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData

# Connect using SQLAlchemy
engine = create_engine("sqlite:///books.db")
metadata = MetaData()
books_table = Table("books", metadata,
                    Column("title", String),
                    Column("author", String),
                    Column("year", Integer))

# Execute query
with engine.connect() as connection:
    result = connection.execute(select(books_table.c.title).order_by(books_table.c.title))
    for row in result:
        print(row[0])
