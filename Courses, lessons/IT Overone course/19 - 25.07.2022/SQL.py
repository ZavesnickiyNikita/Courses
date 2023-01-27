import sqlite3

# Создаем базу данных
conn = sqlite3.connect('name4.db')

# Создаем объект cursor, который позволяет взаимодействовать с базой данных записи
cursor = conn.cursor()

# Создаем таблицу с двумя текстовыми колонками              Вместо TEXT нужно писать INTEGER, если числа
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')

#  Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('hello', 'world')''')

#  Сохраняем изменения
conn.commit()

d = "red"
f = "black"
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES(?,?)''', (d, f))
conn.commit()

# Удаление записи из таблицы по id, по значению
cursor.execute('''DELETE FROM tab_1  WHERE id = 3''')
conn.commit()
cursor.execute('''DELETE FROM tab_1 WHERE col_1 = 'red' ''')
conn.commit()

# Обновление данных в таблице
t = 5
cursor.execute('''UPDATE tab_1 SET col_1 = 'sky' WHERE id = ?''', (t,))
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
print(cursor.fetchall())