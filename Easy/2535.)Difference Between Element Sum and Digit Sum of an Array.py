def difference_of_sum(nums: list[int]):
    counter = 0
    for num in nums:
        counter += helper(num)
    return abs(sum(nums) - counter)


def helper(number: int):
    counter = 0
    while number:
        number, rest = divmod(number, 10)
        counter += rest
    return counter


print(difference_of_sum([1, 15, 6, 3]))
print(difference_of_sum([1, 2, 3, 4]))