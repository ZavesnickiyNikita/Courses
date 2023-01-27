for i in range(5):    # Else выполняется только когда цикл закончился сам
    print(i)
    if i == 3:    # Else не выполняется, когда цикл закончился принудительно
        break
else:               # его остановили Break и в for и в while
    print('Готово')

# i = 0
# while i < 3:
#     print(i)
#     i = i + 1
# else:
#     print('Готово')