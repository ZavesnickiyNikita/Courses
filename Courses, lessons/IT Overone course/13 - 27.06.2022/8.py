#  11.	 Создай список, замени первый его элемент на [1, 2, 3], затем в конец списка добавь сумму
#  элементов вложенного списка.
import random

a = [random.randint(1, 51) for i in range(5)]
print(a)

a[0] = [1, 2, 3]

a.append(sum(a[0]))

print(a)