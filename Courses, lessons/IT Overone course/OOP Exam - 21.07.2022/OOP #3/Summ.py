def valid_int_parameters(func):
    def wrapper_arguments(num1, num2):
        is_valid_1 = isinstance(num1, int) or isinstance(num1, float)
        is_valid_2 = isinstance(num2, int) or isinstance(num2, float)
        if is_valid_1 and is_valid_2:
            print('Is valid')
        else:
            raise Exception('Not a valid')
        print(func(num1, num2))
    return wrapper_arguments

@valid_int_parameters
def summ(num1, num2):
    return num1 + num2


summ(5, 9)