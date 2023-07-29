def missing_number(nums: list[int]):
    diapason = set(range(len(nums)+1))
    nums = set(nums)
    for i in diapason:
        if i not in nums:
            return i


print(missing_number([3, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
