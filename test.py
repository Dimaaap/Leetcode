def two_sum(nums: list[int], target: int):
    seen = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], index]
        seen[num] = index


print(two_sum([2, 7, 11, 15], 9))
