from ast import Try
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

data = [('Равиль, ')]
with con:
    con.executemany(sql, data) # EXECUTE - ДОБАВЛЕНИЕ ДАННЫХ(1 пользователь)
    
#cur.execute("SELECT * FROM users;")
#all_users = cur.fetchall()
client_login = ''

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
        #interests = input('Введите ваши интересы')
        break
           
def login():
    while True:
        try:
            l_login = str(input('введите логин '))
            cur.execute(f"SELECT * FROM users WHERE ulogin='{l_login}';")
            if not cur.fetchone():
                print('Не удалось найти такой аккаунт')
            else:
                print('Здравствуйте, введите пароль')
                l_password = str(input('Введите пароль'))
                if not cur.execute(f"SELECT * FROM users WHERE upassword='{l_password}';"):
                    print("Неправильный пароль")
                else:
                    print('Вы успешно вошли')
                    client_login = l_login
            break
        except Exception:
            print('Ошибка логина или пароля')
    
        
def delete_account(): 
    #всплывающее окно предупреждений
    cur.execute(f"DELETE FROM users WHERE login = '{client_login}';")
    con.commit()
    
def find_friends(): #функция сравнения интересов
    for friend in all_users:
        pass



    