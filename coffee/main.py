import sqlite3

# Подключение к БД
con = sqlite3.connect("Coffee.sqlite")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM coffee""").fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem)

con.close()