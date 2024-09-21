def get_sneaky_numbers(nums: list[int]) -> list[int]:
    seen = set()
    res = []
    for num in nums:
        if num in seen:
            res.append(num)
        else:
            seen.add(num)
    return res


print(get_sneaky_numbers([0, 1, 1, 0]))
print(get_sneaky_numbers([0, 3, 2, 1, 3, 2]))
print(get_sneaky_numbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))