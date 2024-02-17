def find_max_average(nums: list[int], k: int):
    cur = sum(nums[:k])
    cur_max = cur
    for i in range(k, len(nums)):
        cur -= nums[i-k]
        cur += nums[i]
        cur_max = max(cur_max, cur)
    return cur_max / k


print(find_max_average([1, 12, -5, -6, 50, 3], 4))
print(find_max_average([5], 1))