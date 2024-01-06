def two_sum(numbers: list[int], target: int):
    seen = {}
    for index, num in enumerate(numbers):
        if num in seen:
            return [seen[num], index+1]
        else:
            seen[target - num] = index + 1
    return "Wow"


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([2, 3, 4], 6))
print(two_sum([-1, 0], -1))
