# import requests
# from bs4 import BeautifulSoup
# import sqlite3  # импортируем модуль для работы с SQLite
# from datetime import datetime  # импортируем модуль для работы с датой/временем
#
# # создадим подключение к SQLite-базе, создадим таблицу, если она не существует
# con = sqlite3.connect("windows_store.db")   # con - connection (подключение)
# cur = con.cursor()   # cur - cursor (курсор)
# cur.execute("CREATE TABLE IF NOT EXISTS apps (name TEXT, company TEXT, release_year INTEGER, email TEXT)")
#
#
# url = 'https://apps.microsoft.com/store/category/Business'   # url - link (ссылка)
# response = requests.get(url).text   # response - response (ответ)
# soup = BeautifulSoup(response, 'lxml')   # soup - soup (суп)
#
#
# for item in soup.find_all('div', class_="mj33-card"):    # item - item (элем.)
#
#     name = item.find('div', class_="mj33-card__heading").text    # name - name (назв.)
#
#     company = item.find('div', class_="mj33-card__subtitle").text    # company - company (ком.)
#
#     try:     # try - try / except - except (пыт./иск.)
#         release_year = int(item.find('span', class_="mj33-release-year").text[1:-1])     # release year - year of release (вых.)
#
#     except AttributeError:     # attribute error - error of attribute (ошибка атриб.)                                                             release_year = None
#
#     email = item.find('a', class_="mj33-contact")['href'][7:]   # email - electronic mail (эл.-я.)
#
#     cur.execute("INSERT INTO apps VALUES (?, ?, ?, ?)", [name, company, release_year, email])   # execute command to insert data into the table ('apps')     con.commit()   # commit the changes to the database ('windows store')     con.close()