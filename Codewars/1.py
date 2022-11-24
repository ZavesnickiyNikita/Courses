def eq_sum_powdig(hMax, exp):
    result = []
    for num in range(2, hMax + 1):
        ls = []
        total_list = []
        nums = num
        while num != 0:
            ls.append(num % 10)
            num = num // 10
        for i in ls:
            total_list.append(i ** exp)
        if sum(total_list) == nums:
            result.append(nums)
    return result


print(eq_sum_powdig(100, 2))
print(eq_sum_powdig(1000, 2))
print(eq_sum_powdig(200, 3))
print(eq_sum_powdig(370, 3))


