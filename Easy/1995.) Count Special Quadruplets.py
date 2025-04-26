def count_quadruplets(nums: list[int]) -> int:
    """
    Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
        nums[a] + nums[b] + nums[c] == nums[d], and
        a < b < c < d
    """
    counter = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for u in range(k + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == nums[u]:
                        counter += 1
    return counter


print(count_quadruplets([1, 2, 3, 6]))
print(count_quadruplets([3, 3, 6, 4, 5]))
print(count_quadruplets([1, 1, 1, 3, 5]))