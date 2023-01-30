# Импорт нужных библиотек
import requests
from bs4 import BeautifulSoup
import sqlite3

# Создаем базу данных и подключаемся к ней
conn = sqlite3.connect('appstore.db')
c = conn.cursor()   

# Нужно создать таблицу и записать в нее данные
c.execute("CREATE TABLE appstore (name text, company text, release_year text, email text)")

# Делаем запрос на странице с приложениями и парсим результат до тех пор, пока не закончится категория
url = "https://apps.microsoft.com/store/category/Business"
i = 0
while url and i < 200:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    app_info = soup.find_all('div', {'class': 'app info'})

    for app in app_info:
        try:
            name = app.find('a', {'class': 'app-title'}).text
            company = app.find('div', {'class': 'app-all-info'}).text
            release_year = app.find('div', {'class': 'app-publisher'}).text
            email = app.find('div', {'class': 'app-support-container'}).text
        except AttributeError:
            pass
        else:
            c.execute("INSERT INTO appstore (name, company, release_year, email) VALUES (?, ?, ?, ?)",
                      (name, company, release_year, email))
            conn.commit()
            i += 1

    # Обновляем URL, чтобы достать данные из других приложений
    el = soup.find("a", {"class": "see-more-arrow"})
    if el:
        url = el.attrs.get("href")

# Закрываем соединение с базой данных
conn.close()

# Создаем HTML страницу, на которую будут добавлены записи из базы данных
f = open('appstore.html', 'w')

# Текстовое поле и кнопка фильтрации
message = """<!DOCTYPE html>
<head>
<title>App screenshot data</title>
</head><body>
<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search by company..">
<button onclick="myFunction()">Filter</button>
<table id="myTable">
<tr class="header">
    <th style="width:35%;">Name</th>
    <th style="width:25%;">Company</th>
    <th style="width:20%;">Release year</th>
    <th style="width:20%;">Email</th>
  </tr>"""
f.write(message)

# Подключаемся к базе данных и загружаем данные
conn = sqlite3.connect('appstore.db')
c = conn.cursor()
query = c.execute('SELECT * FROM appstore')

# Записываем данные из базы данных в HTML страницу
for row in query.fetchall():
    message = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (row[0], row[1], row[2], row[3])
    f.write(message)

# Закрываем поток записи в файл
f.write('</table></body></html>')
f.close()

# Закрываем соединение с базой данных
conn.close()