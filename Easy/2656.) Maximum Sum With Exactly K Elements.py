def maximize_sum(nums: list[int], k: int):
    ans = 0
    i = 0
    while i < k:
        max_el = max(nums)
        ans += max_el
        nums.remove(max_el)
        nums.append(max_el + 1)
        i += 1
    return ans


print(maximize_sum([1, 2, 3, 4, 5], 3))
print(maximize_sum([5, 5, 5], 2))