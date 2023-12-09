def find_max(nums: list[int]):
    ans = -1
    for n in nums:
        if n * -1 in nums:
            ans = max(n, ans)
    return ans


print(find_max([-1, 2, -3, 3]))
print(find_max([-1, 10, 6, 7, -7, 1]))
print(find_max([-10, 8, 6, 7, -2, -3]))
