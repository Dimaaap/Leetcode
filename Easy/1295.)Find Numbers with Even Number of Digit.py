def find_numbers(nums: list[int]):
    counter = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            counter += 1
    return counter


print(find_numbers([12, 345, 2, 6, 7896]))
print(find_numbers([555, 901, 482, 1771]))