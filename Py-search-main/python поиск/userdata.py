from ast import Try
from re import U
import sqlite3 as sl

con = sl.connect('userdata.db') #подключение базы данных к коду
cur = con.cursor() #курсор для навигации по базе данных

#создание и конфигурация базы данных

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
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

data = [(1, 'Равиль', 16, 'мужчина', '@ravil123', 'FOOTBALL, STREETBALL, VOLLEYBALL, YAY CORN',
        'ravil123', 'password123'),
        (2, 'Bentley', 17, 'ЖЕНЩИНА', '@govno', 'FOOTBALL, GAMES, MARIO', 'Bentley123',
         'password123')] #пример данных пользователя
with con:
    con.executemany(sql, data) # EXECUTE - ДОБАВЛЕНИЕ ДАННЫХ(1 пользователь)


cur.execute("SELECT * FROM users;")
all_users = cur.fetchall()
client_login = ''
client_password = ''
client_interests = ''

def registration():
    while True: #1
        u_login = input('ВВЕДИТЕ ЛОГИН')
        if ' ' in u_login:
            print('Упс! Вы ввели логин неправильно. В логине не должно быть пробелов')
        if len(u_login) > 14:
            print('Упс! Длина логина не должна быть больше 14 символов')
        else:
            break
    while True: #2
        u_password = input('Введите ваш пароль')
        if len(u_password) <= 8:
            print('Упс! Длина пароля должна быть больше 8') 
        else:
            break
    name = input('ВВЕДИТЕ ИМЯ') #3
    while True: #4
        try:
            age = int(input('ВВЕДИТЕ ВАШ ВОЗРАСТ'))
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
        telegram = input('Введите id вашего телеграм аккаунта(ОБЯЗАТЕЛЬНО)')
        #Должна быть проверка на уникальность id
        break
    while True: #7
        interests = input('''Введите ваши интересы через запятую + пробел'
                             Например: "Football, sports, games"''')
        break
           
def login():
    global all_users, client_login, client_password
    while True:
        try:
            l_login = str(input('введите логин '))
            cur.execute(f"SELECT * FROM users WHERE ulogin='{l_login}';")
            if not cur.fetchone():
                print('Не удалось найти такой аккаунт')
            else:
                print('Здравствуйте, введите пароль')
                l_password = str(input('Введите пароль: '))
                if not cur.execute(f"SELECT * FROM users WHERE upassword='{l_password}';"):
                    print("Неправильный пароль")
                else:
                    print('Вы успешно вошли')
                    client_login = l_login
                    client_password = l_password
                    cur.execute(f'SELECT * FROM users WHERE ulogin="{l_login}" ')
                    user_data = cur.fetchone()
                    all_users.remove(user_data)
            break
        except Exception:
            print('Ошибка логина или пароля')
    
        
def delete_account(): 
    #тут должно выскакивать всплывающее окно предупреждений
    cur.execute(f"DELETE FROM users WHERE login = '{client_login}';")
    con.commit()
    
def find_friends(): #функция сравнения интересов
    interests_match = 0
    for user in all_users:
        user_interest = user[5]
        user_interest = user_interest.split(', ')
        print(user_interest)
        for interest in user_interest:
            for c_interest in client_interests:
                if interest == c_interest:
                    interests_match += 1
    if interests_match >= 3:
        print(f'Найдено совпадение с пользователем {user[2]}')
        return 1
    else:
        return 0
login()
find_friends()


    