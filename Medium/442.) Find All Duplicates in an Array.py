def find_duplicates(nums: list[int]):
    result = []
    for num in nums:
        num = abs(num)
        if nums[num - 1] < 0:
            result.append(num)
        else:
            nums[num - 1] = -nums[num - 1]
    return result


print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_duplicates([1, 1, 2]))
print(find_duplicates([1]))
