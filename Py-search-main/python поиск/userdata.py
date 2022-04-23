from ast import Try
from pydoc import cli
from re import S, U
import sqlite3 as sl

con = sl.connect('userdata.db') #подключение базы данных к коду
cur = con.cursor() #курсор для навигации по базе данных

#создание и конфигурация базы данных

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            telegram TEXT UNIQUE,
            interests TEXT NOT NULL,
            ulogin TEXT NOT NULL UNIQUE,
            upassword TEXT NOT NULL
        );
    """)

sql = '''INSERT or REPLACE INTO users (id, name, age, gender, telegram, interests, ulogin, upassword) 
                                       values(?, ?, ?, ?, ?, ?, ?, ?)'''

data = [(1, 'Равиль', 16, 'мужчина', '@ravil123', 'FOOTBALL, STREETBALL, VOLLEYBALL, CORN',
        'ravil123', 'password123'),
        (2, 'Bentley', 17, 'женщина', '@Bentley123', 'FOOTBALL, GAMES, MARIO', 'Bentley123',
         'password123'),
        (3, 'Volvo', 16, 'мужчина', '@Volvo123', 'FOOTBALL, STREETBALL, CORN', 'Volvo123',
         'password123'),
        (4, 'volkswagen', 19, 'мужчина', '@volkswagen123', 'FOOTBALL, BOOKS, FILMS, COMICS', 'volkswagen123',
         'password123'),
        (5, 'bmw', 20, 'женщина', '@bmw123', 'FOOTBALL, CORN, VOLLEYBALL', 'bmw123',
         'password123')] #пример данных пользователя
with con:
    con.executemany(sql, data) # EXECUTE - ДОБАВЛЕНИЕ ДАННЫХ(1 пользователь)


cur.execute("SELECT * FROM users;")
all_users = cur.fetchall()
client_login = ''
client_password = ''
client_interests = []

def registration():
    global sql
    while True: #1
        r_login = input('Введите логин: ')
        cur.execute(f"SELECT * FROM users WHERE ulogin='{r_login}';")
        if cur.fetchone():
            print('Такой логин уже занят')
        elif ' ' in r_login or len(r_login) > 14:
            print('Упс! Вы ввели логин неправильно. В логине не должно быть пробелов, '
            'также длина логина не должна быть больше 14 символов')
        else:
            break
    while True: #2
        r_password = input('Введите ваш пароль: ')
        if len(r_password) <= 8:
            print('Упс! Длина пароля должна быть больше 8') 
        else:
            break
    r_name = input('Введите имя: ') #3
    while True: #4
        try:
            age = int(input('Введите ваш возраст: '))
            if age < 14:
                print('Ой! Похоже, вы слишком малы для этого приложения')
            else:
                break
        except ValueError:
            print('ВВЕДИТЕ ЧИСЛО')
    while True: #5
        gender = str(input('Введите ваш пол(мужчина или женщина): ').lower().replace(' ', ''))
        if gender != 'мужчина' and gender != 'женщина':
            print('введите корректный пол')
        else:
            break
    while True: #6
        telegram = input('Введите id вашего телеграм аккаунта(ОБЯЗАТЕЛЬНО): ')
        #Должна быть проверка на уникальность id
        break
    while True: #7
        interests = input('Введите ваши интересы через запятую + пробел'
                          'Например: "Football, sports, games". ').upper()
        break
    registration_user = (10, f'{r_name}', f'{age}', f'{gender}', f'{telegram}', f'{r_login}', f'{r_password}', f'{interests}')
    with con:
        cur.execute(sql, registration_user)
    cur.execute(f"SELECT * FROM users WHERE ulogin='{r_login}';")
    if cur.fetchone():
        print("Аккаунт создан ")
    else:
        print('ОШИБКА')
           
def login():
    global all_users, client_login, client_password, client_interests
    while True:
        try:
            l_login = str(input('введите логин: '))
            cur.execute(f"SELECT * FROM users WHERE ulogin='{l_login}';")
            if not cur.fetchone():
                print('Не удалось найти такой аккаунт')
            else:
                print('Здравствуйте, введите пароль')
                l_password = str(input('Введите пароль: '))
                cur.execute(f"SELECT * FROM users WHERE upassword='{l_password}';")
                if not cur.fetchone():
                    print("Неправильный пароль")
                else:
                    print('Вы успешно вошли')
                    print('=========================================================')
                    client_login = l_login
                    client_password = l_password
                    cur.execute(f'SELECT * FROM users WHERE ulogin="{l_login}" ')
                    user_data = cur.fetchone()
                    all_users.remove(user_data)
                    client_interests = user_data[5].split(', ')
            break
        except Exception:
            print('Ошибка логина или пароля')
    
        
def delete_account(): 
    #тут должно выскакивать всплывающее окно предупреждений
    cur.execute(f"DELETE FROM users WHERE login = '{client_login}';")
    con.commit()
    
def find_friends(): #функция сравнения интересов
    for user in all_users:
        interests_match = 0
        user_interest = user[5]
        user_interest = user_interest.split(', ')
        for interest in user_interest:
            for c_interest in client_interests:
                if interest == c_interest:
                    interests_match += 1
        if interests_match >= 3:
            interests_match = interests_match/len(client_interests) * 100
            print(f'Найдено совпадение с пользователем {user[1]} ||',
                  f'Совпадений: {interests_match}%')
        else:
            pass
login()
find_friends()


    