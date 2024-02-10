def return_to_boundary_count(nums: list[int]):
    boundary = 0
    count = 0
    for num in nums:
        boundary += num
        if boundary == 0:
            count += 1
    return count


print(return_to_boundary_count([2, 3, -5]))
print(return_to_boundary_count([3, 2, -3, -4]))