def average_value(nums: list[int]):
    num_sum, count = 0, 0
    for n in nums:
        if n % 2 == 0 and n % 3 == 0:
            num_sum += n
            count += 1
    if count == 0:
        return 0
    return int(num_sum / count)


print(average_value([1, 3, 6, 10, 12, 15]))
print(average_value([1, 2, 4, 7, 10]))