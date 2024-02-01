import sqlite3

with sqlite3.connect('students.db') as con:
    cur = con.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  surname TEXT,
  hobby TEXT,
  birth_year INTEGER,
  homework_grade INTEGER
    )''')

    cur.execute('''INSERT INTO students VALUES (NULL,'Beka','Alimov', 'football', 1999, 9)''')
    cur.execute('''INSERT INTO students VALUES (NULL,'Tanzila','Nurlanova', 'dance', 2002, 10)''')
    cur.execute('''INSERT INTO students VALUES (NULL,'Aikan','Maksytova', 'sing', 2003, 2)''')
    cur.execute('''INSERT INTO students VALUES (NULL,'Maria','Akylova', 'volleyball', 2001, 7)''')
    cur.execute('''INSERT INTO students VALUES (NULL,'Malika','Sultanova', 'listen music', 2004, 5)''')
    cur.execute('''INSERT INTO students VALUES (NULL,'Amaliya','Bolotekova', 'cooking', 2007, 8)''')
    cur.execute('''INSERT INTO students VALUES (NULL,'Maksat','Karybaev','boxing', 2000, 6)''')
    cur.execute('''INSERT INTO students VALUES (NULL,'Beksultan','Abdalov', 'struggle', 1998, 1)''')
    cur.execute('''INSERT INTO students VALUES (NULL,'Aidana','Alikenova', 'programming', 2003, 3)''')
    cur.execute('''INSERT INTO students VALUES (NULL,'Marat','Nurlanbekov', 'football', 2002, 4)''')

    cur.execute("""SELECT * FROM students WHERE surname > '10'""")
    cur.execute("""UPDATE students SET name = 'genius' WHERE homework_grade > 10""")
    cur.execute("""SELECT * FROM students WHERE name = 'genius'""")
    cur.execute("""DELETE FROM students WHERE id % 2 = 0""")

    # Вывод данных
    for row in cur:
        print(row)