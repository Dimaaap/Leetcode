def contains_nearby_duplicate(nums: list[int], k: int):
    seen = {}
    for index, num in enumerate(nums):
        if num not in seen:
            seen[num] = index
        else:
            distinct = abs(index - seen[num])
            if distinct <= k:
                return True
            seen[num] = index
    return False


print(contains_nearby_duplicate([1, 2, 3, 1], 3))
print(contains_nearby_duplicate([1, 0, 1, 1], 1))
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))
print(contains_nearby_duplicate([99, 99], 2))
