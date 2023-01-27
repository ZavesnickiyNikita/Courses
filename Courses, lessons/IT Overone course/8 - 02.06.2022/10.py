# Дописать скрипт для расчета средней температуры

week_temp = (26, 29, 34, 32, 28, 26, 23, 28, 32, 19)
sum_temp = sum(week_temp)
days = len(week_temp)
print(days, 'Количество дней')
mean_temp = sum_temp / days
print(int(mean_temp), 'Средняя температура за период')