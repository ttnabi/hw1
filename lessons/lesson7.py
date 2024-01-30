# база данных 2 типа
# MySQL,posgreSQL, SQLite3
# SQL
# СУБД-система управления базами данных
# CRUD-create reed update delete
# sqlite3 - connect - cursor - execute
# ограничители NOT NULL DEFAULT 0
import sqlite3
with sqlite3.connect('op38.db') as con:
    cur = con.cursor()
    # cur.execute('''DROP TABLE users''')
    cur.execute(''' CREATE TABLE IF NOT EXISTS users(
    name TEXT NOT NULL,
    view INTEGER NOT NULL DEFAULT 5,
    age INT DEFAULT 1
    )''')
#crud = api-CREATE
    # cur.execute('''INSERT INTO users VALUES ('BEKA',30,8)''')
    # cur.execute('''INSERT INTO users (name) VALUES ('name')''')

    cur.execute('''SELECT rowid,* FROM users ORDER BY rowid desc ''')
    print('id name view age')
    for i in cur.fetchall():
        print(i)

#reed


# con=with sqlite3.connect('op38.db')