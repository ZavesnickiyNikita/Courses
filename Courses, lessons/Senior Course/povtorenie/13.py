li = [input() for i in range(3)]
result_en = all(map(lambda x: True if x in "AaBCcEeHKMOoPpTXxy" else False, li))
result_ru = all(map(lambda x: True if x in "АаВСсЕеНКМОоРрТХху" else False, li))
if result_en:
    print('en')
if result_ru:
    print('ru')
if not result_en and not result_ru:
    print('mix')