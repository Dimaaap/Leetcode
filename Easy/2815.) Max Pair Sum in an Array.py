def max_sum(nums: list[int]):
    """
    You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of
    numbers from nums such that the maximum digit in both numbers are equal.
    Return the maximum sum or -1 if no such pair exists
    """
    ans = -1
    visited = {}
    nums.sort()
    for num in nums:
        max_set_num = max(set(str(num)))
        if int(max_set_num) not in visited:
            visited[int(max_set_num)] = [num]
        else:
            visited[int(max_set_num)].append(num)
    for key, value in visited.items():
        if len(value) >= 2:
            for i in range(len(value)-1):
                ans = max(ans, value[i] + value[i + 1])
    return ans


print(max_sum([51, 71, 17, 24, 42]))
print(max_sum([1, 2, 3, 4]))
print(max_sum([31, 25, 72, 79, 74]))
