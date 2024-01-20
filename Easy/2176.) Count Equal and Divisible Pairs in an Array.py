def count_pairs(nums: list[int], k: int):
    counter = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and (i * j) % k == 0:
                counter += 1
    return counter


print(count_pairs([3, 1, 2, 2, 2, 1, 3], 2))
print(count_pairs([1, 2, 3, 4], 1))
print(count_pairs([5, 5, 9, 2, 5, 5, 9, 2, 2, 5, 5, 6, 2, 2, 5, 2, 5, 4, 3], 7))
