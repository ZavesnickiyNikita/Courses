def index_of_nearest(nums, n):
    if nums:
        minimum = min(nums, key=lambda num: abs(num - n))
        return nums.index(minimum)
    return -1





print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))


