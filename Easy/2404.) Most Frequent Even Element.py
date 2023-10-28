def most_frequent_even(nums: list[int]):
    max_count = 0
    number = -1
    for num in nums:
        if num % 2 == 0:
            if nums.count(num) == max_count and num < number:
                number = num
            if nums.count(num) > max_count:
                max_count = nums.count(num)
                number = num
    return number


print(most_frequent_even([0, 1, 2, 2, 4, 4, 1]))
print(most_frequent_even([4, 4, 4, 9, 2, 4]))
print(most_frequent_even([29, 47, 21, 41, 13, 37, 25, 7]))
print(most_frequent_even([8154, 9139, 8194, 3346, 5450, 9190, 133, 8239, 4606, 8671, 8412, 6290]))
print(most_frequent_even([2, 10000, 10000, 10000, 2]))
