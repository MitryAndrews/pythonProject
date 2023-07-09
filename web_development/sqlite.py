import sqlite3 as sql

connection = sql.connect('test.sqlite')
q = connection.cursor() # с помощью этого курсора мы можем добавлять, получать данные

# Создаем таблицу на языке SQL, описываем желание сделать действия
# q.execute('''CREATE TABLE user (id int auto_increment primary key, name varchar, password varchar)''')
# далее нужно дать команду на производство операции
# connection.commit()

user_name = input('Введите ваше имя: ')
user_password = input('Введите пароль: ')
print('Список пользователей: \n')
q.execute("INSERT INTO user (name, password) VALUES ('%s', '%s')"%(user_name, user_password))
connection.commit()
q.execute("SELECT * FROM user")
# если мне просто вывести что-то из БД, то команду commit не нужно делать
row = q.fetchone() # пользователь в виде списка, где индекс [0] это id индекс [1] имя и [2] пароль
# с помощью цикла while мы просто что-то делаем с данными пользователя например печатаем
while row is not None:
    print('Name ', row[1], '| Password ', row[2])
    row = q.fetchone()

# Отключение от БД, это как в файлах - открыли файл, то потом нужно закрыть
# Сначала закрываем курсор, а потом и базу
q.close()
connection.close()


