import test
import tests

def next_numb(val):
    for i in range(val, 10 ** 7):
        if i % 2 == 0 and i // 3 == 0:
            return next_number




test.assert_equals(next_numb(12), 15)
