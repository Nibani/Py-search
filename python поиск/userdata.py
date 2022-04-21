import sqlite3 as sl
import os


con = sl.connect('userdata.db')
cur = con.cursor()

#создание таблицы

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            telegram TEXT UNIQUE,
            interests TEXT NOT NULL
        );
    """)

sql = 'INSERT or REPLACE INTO users (id, name, age, gender, telegram, interests) values(?, ?, ?, ?, ?, ?)'
data = []

with con:
    con.executemany(sql, data) # EXECUTE - ДОБАВЛЕНИЕ ДАННЫХ(1 пользователь)
cur.execute("SELECT * FROM users;")
all_users = cur.fetchall()

def registration():
    pass
def delete_account():
    pass
def find_friends():
    for friend in all_users:
        for i in range(len(all_users)):
            friends_interests = all_users[i][5]


    