def find_middle_index(nums: list[int]):
    for i in range(len(nums)):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i+1:])
        if left_sum == right_sum:
            return i
    return -1


print(find_middle_index([2, 3, -1, 8, 4]))
print(find_middle_index([1, -1, 4]))
print(find_middle_index([2, 5]))