
class Calculator:
    def valdate_numbers(self, first_number, second_number):
        is_valid_first_number = isinstance(first_number, int) or isinstance(first_number, float)
        is_valid_second_number = isinstance(second_number, int) or isinstance((second_number, float))
        if is_valid_first_number and is_valid_second_number:
            print('Valid')
        else:
            # print('Not valid')
            raise Exception ('Not Valid')   # Вызвать ошибку

    def summ(self, first_number, second_number):
        self.valdate_numbers(first_number, second_number)
        summ = first_number + second_number
        return summ

    def difference(self, first_number, second_number):
        self.valdate_numbers(first_number, second_number)
        diff = first_number - second_number
        return diff

    def multiplication(self, first_number, second_number):
        self.valdate_numbers(first_number, second_number)
        multip = first_number * second_number
        return multip

    def division(self, first_number, second_number):
        self.valdate_numbers(first_number, second_number)

        if second_number == 0:
            return('It cannot be divided by 0')
        else:
            div = first_number / second_number
            return (div)

my_caltculator = Calculator()
print(my_caltculator.summ(5, 2))
print(my_caltculator.difference(5, 2))
print(my_caltculator.multiplication(5, 2))
print(my_caltculator.division(1, 0))