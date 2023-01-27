# Задача про треугольник
import random
question = float(input("Сколько сторон вы хотите ввести?"))
if question != 3:
    print("Это не треугольник ")
else:
    print("Молодец, продолжаем")
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,100)
    print(a,b,c, "\n")
    if a == b and b == c and a == c:
        print("Равносторонний треугольник")
    elif a == b or b == c or a == c:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")