n = int(input())
amount_3 = 0
amount_last_number = 0
amount_chetnih = 0
summa_bolshe_5 = 0
amount_0_and_5 = 0
proizvedenoe_bolshih_7 = 1
last_digit = 0
last = n % 10
while n != 0:
    last_digit = n % 10
    n //= 10
    if last_digit == 3:
        amount_3 += 1
    if last_digit == last:
        amount_last_number += 1
    if last_digit % 2 == 0:
        amount_chetnih += 1
    if last_digit > 5:
        summa_bolshe_5 += last_digit
    if last_digit > 7:
        proizvedenoe_bolshih_7 *= last_digit
    if last_digit in (0, 5):
        amount_0_and_5 += 1
print(amount_3)
print(amount_last_number)
print(amount_chetnih)
print(summa_bolshe_5)
print(proizvedenoe_bolshih_7)
print(amount_0_and_5)








