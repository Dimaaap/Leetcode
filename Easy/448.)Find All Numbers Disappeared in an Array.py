def find_disappear_number(nums: list[int]):
    return list(set(range(1, len(nums)+1)) - set(nums))


print(find_disappear_number([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_disappear_number([1, 1]))

