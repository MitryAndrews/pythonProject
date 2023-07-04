import sqlite3 as sql

connection = sql.connect('test.sqlite')
q = connection.cursor() # с помощью этого курсора мы можем добавлять, получать данные

# Создаем таблицу на языке SQL, описываем желание сделать действия
q.execute('''CREATE TABLE user (id int auto_increment primary, name varchar, password varchar)''')
# далее нужно дать команду на производство операции
connection.commit()

user_name = input('Введите ваше имя: ')
user_password = input('Введите пароль: ')
print('Список пользователей: \n')
q.execute("INSERT INT0 user (name, password) VALUES ('%s', '%s')%(user_name, user_password")

# Отключение от БД, это как в файлах - открыли файл, то потом нужно закрыть
# Сначала закрываем курсор, а потом и базу
q.close()
connection.close()


