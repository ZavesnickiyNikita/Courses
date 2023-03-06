

import requests
from bs4 import BeautifulSoup

url = "https://apps.microsoft.com/store/category/business"

# получаем страницу
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# находим все теги с названием приложения, разработчиком, годом релиза и электронной почтой
app_titles = soup.find_all('h2', class_="c-heading-2")
developer_names = soup.find_all('div', class_="c-listing-tile-v2__subtitle")
release_years = soup.find_all('span', class_="c-listing-tile-v2__release-date")
emails = soup.find_all('a', class_="c-listing-tile-v2__contact-email")

# записываем результат парсинга в HTML файл
with open('parsed_apps.html', 'w') as f:
    f.write('<html><body>')
    for i in range(len(app_titles)):
        f.write(f"<h2>Название приложения: {app_titles[i].text}</h2>")
        f.write(f"<div>Название компании производителя: {developer_names[i].text}</div>")
        f.write(f"<span>Год релиза: {release_years[i].text}</span>")
        try:
            f.write(f"<a>Email: {emails[i].text}</a>")
        except:
            f.write("<a>Email отсутствует</a>")
        f.write('<hr>')
    f.write('</body></html>')