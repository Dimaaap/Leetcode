def left_right_difference(nums: list[int]):
    ans = []
    for i in range(len(nums)):
        left_sum = right_sum = 0
        if nums[:i]:
            left_sum = sum(nums[:i])
        if nums[i:]:
            right_sum = sum(nums[i+1:])
        ans.append(abs(left_sum - right_sum))
    return ans


print(left_right_difference([10, 4, 8, 3]))
print(left_right_difference([1]))

