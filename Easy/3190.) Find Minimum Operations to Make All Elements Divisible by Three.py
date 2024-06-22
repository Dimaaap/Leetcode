def minimum_operations(nums: list[int]) -> int:
    i = 0
    operations = 0
    while i < len(nums):
        if nums[i] % 3 == 0:
            nums.pop(i)
            continue
        else:
            if nums[i] + 1 % 3 == 0:
                nums[i] += 1
                operations += 1
            else:
                nums[i] -= 1
                operations += 1
        i += 1
    return operations



print(minimum_operations([1, 2, 3, 4]))
print(minimum_operations([3, 6, 9]))

