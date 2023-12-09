def count_k_difference(nums: list[int], k: int):
    counter = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                counter += 1
    return counter


print(count_k_difference([1, 2, 2, 1], 1))
print(count_k_difference([3, 2, 1, 5, 4], 2))
