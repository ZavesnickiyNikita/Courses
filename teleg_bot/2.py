from random import *

def number_of_pairs(gloves: list):
    result = []
    
    dct = {}
    for i in gloves:
        dct.setdefault(i, gloves.count(i))

    count = 0
    for i in dct.values():
        count += i // 2
    return count


# print(number_of_pairs(["red", "red", "red"]))
# print(number_of_pairs(["red", "green", "blue"]))
# print(number_of_pairs(["gray", "black", "purple", "purple", "gray", "black"]))
# print(number_of_pairs(["red", "green", "blue",
#       "blue", "red", "green", "red", "red", "red"]))

test.describe("Basic tests")
test.assert_equals(number_of_pairs(["red","red"]),1)
test.assert_equals(number_of_pairs(["red","green","blue"]),0)
test.assert_equals(number_of_pairs(["gray","black","purple","purple","gray","black"]),3)
test.assert_equals(number_of_pairs([]),0)
test.assert_equals(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]),4)
