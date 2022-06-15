import sqlite3

db = sqlite3.connect('C:\\SQLite\\1.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS cakes (
    name VARCHAR(30),
    description VARCHAR(30),
    price MONEY
)""")

db.commit()

cakes_name = input('Name: ')
cakes_description = input('Description: ')

sql.execute(f"SELECT name FROM cakes WHERE name = '{cakes_name}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO cakes VALUES ('{cakes_name}', '{cakes_description}', {2000})")
    db.commit()
else:
    print('Такая запись уже есть')