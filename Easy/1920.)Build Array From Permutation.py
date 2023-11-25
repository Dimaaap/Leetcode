def build_array(nums: list[int]):
    ans = []
    for i in nums:
        ans.append(nums[i])
    return ans


print(build_array([0, 2, 1, 5, 3, 4]))
print(build_array([5, 0, 1, 2, 3, 4]))
