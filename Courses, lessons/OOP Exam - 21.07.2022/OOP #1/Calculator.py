class Calculator:

    def valdate_numbers(self, first_number, second_number):
        is_valid_first_number = isinstance(first_number, int) or isinstance(first_number, float)
        is_valid_second_number = isinstance(second_number, int) or isinstance((second_number, float))
        if is_valid_first_number and is_valid_second_number:
            print('Valid')
        else:
            raise Exception('Not Valid')

    def summ(self, first_number, second_number):
        self.valdate_numbers(first_number, second_number)
        sum = first_number + second_number
        print(sum)

    def difference(self, first_number, second_number):
        self.valdate_numbers(first_number, second_number)
        diff = first_number - second_number
        print(diff)

    def multiplication(self, first_number, second_number):
        self.valdate_numbers(first_number, second_number)
        mult = first_number * second_number
        print(mult)

    def division(self, first_number, second_number):
        self.valdate_numbers(first_number, second_number)

        if second_number == 0:
            print("It's canntot divided by 0")
        else:
            div = first_number / second_number
            print(div)


my_calculator = Calculator()
my_calculator.summ(3, 4)
my_calculator.difference(4, 3)
my_calculator.multiplication(4, 5)
my_calculator.division(12, 0)