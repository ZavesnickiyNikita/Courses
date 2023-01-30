import requests
from bs4 import BeautifulSoup
import sqlite3
from flask import Flask, render_template

# Получение данных с сайта
url = 'https://apps.microsoft.com/store/category/Business'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
data = soup.find_all(class_='app-title')

# Парсинг данных и запись в базу данных
conn = sqlite3.connect('store.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS apps
            (name text, company text, year text, email text)''')

for item in data[:200]:
    link = 'https://apps.microsoft.com' + item.find('a')['href']
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    app_name = item.find('a').text
    company_name = soup.find(class_='app-publisher').text
    release_year = soup.find(class_='app-release-date').text[-4:]
    email = soup.find(class_='email-link')['href'][7:]
    c.execute('''INSERT INTO apps VALUES (?, ?, ?, ?)''', (app_name, company_name, release_year, email))

conn.commit()
conn.close()


# Создание веб-сервера
app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('store.db')
    c = conn.cursor()
    c.execute('SELECT * FROM apps')
    data = c.fetchall()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()