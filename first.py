# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM Films
    WHERE duration >= 60 AND
     genre=(SELECT id FROM genres WHERE title = 'комедия') """).fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem[1])

con.close()
