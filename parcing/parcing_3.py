import requests
from bs4 import BeautifulSoup
import sqlite3

# создаем БД и таблицу
conn = sqlite3.connect('Business_apps.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS apps
                  (title text, company text, release_year text, email text)
               """)

# собираем данные о приложениях с сайта
url = 'https://apps.microsoft.com/store/category/Business'

for i in range(10):  # парсим первые 10 страниц
    response = requests.get(url, params={'Page': i})
    soup = BeautifulSoup(response.text, 'html.parser')
    apps = soup.find_all('div', class_='m-channel-placement-item')

    for app in apps:
        title = app.find('h3', class_='m-channel-placement-item-title').text
        company = app.find('div', class_='m-channel-placement-item-subtitle').text
        release_year = app.find('div', class_='m-channel-placement-item-info-list').find_all('span')[1].text
        email = app.find('div', class_='m-channel-placement-item-info-list').find_all('span')[2].text

        cursor.execute("INSERT INTO apps VALUES (?,?,?,?)", (title, company, release_year, email))

# записываем данные в БД
conn.commit()

# формируем html страницу с таблицей
html = '<html>' \
       '<head>' \
       '<title>Business Apps</title>' \
       '<style>' \
       'table {border-collapse: collapse;}' \
       'th, td {border: 1px solid #ccc;}' \
       '</style>' \
       '</head>' \
       '<body>' \
       '<h1>Business Apps</h1>' \
       '<hr>' \
       '<table>' \
       '<tr>' \
       '<th>Title</th>' \
       '<th>Company</th>' \
       '<th>Release Year</th>' \
       '<th>Email</th>' \
       '</tr>'

# получаем данные из БД и добавляем их в таблицу
cursor.execute("SELECT * FROM apps")
rows = cursor.fetchall()
for row in rows:
    html += '<tr>'
    html += f'<td>{row[0]}</td>'
    html += f'<td>{row[1]}</td>'
    html += f'<td>{row[2]}</td>'
    html += f'<td>{row[3]}</td>'
    html += '</tr>'

html += '</table>' \
        '</body>' \
        '</html>'

# записываем html в файл
with open('Business_apps.html', 'w') as file:
    file.write(html)