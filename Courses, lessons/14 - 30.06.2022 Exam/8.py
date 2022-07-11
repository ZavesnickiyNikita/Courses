#  Работа со словарем Depeche Mode
songsdict = { 'World in My Eyes': 6.56, 'Sweetest Perfection': 4.43, 'Personal Jesus': 4.55, 'Halo': 4.30,
              'Waiting for the Night': 6.07, 'Enjoy the Silence': 6.12, 'Policy of Truth': 4.55,
              'Blue Dress': 5.38, 'Clean': 5.32, 'Dangerous': 4.21, 'Memphisto': 4.09, 'Sibeling': 3.18,
              'Kaleid': 4.18, 'Happiest Girl': 4.58, 'Sea of sin': 4.46}
times = sum(songsdict.values())
list_1 = []
list_keys = []
list_values = []
print('Общее время звучания', times, 'мин.')
for i in songsdict.items():
    if i[1] > 5:
        list_1.append(i[0])
print(list_1, '- список песен, длительность которых больше 5-ти минут.')
print('---------------------------------------------------------------')

for i, j in enumerate(songsdict.items()):
    if ' ' not in j[0]:
        list_keys.append(j[0])
        list_values.append(j[1])

dict_one_word = dict(zip(list_keys, list_values))
print(dict_one_word, '- Словарь песен, название которых из 1 слова')
