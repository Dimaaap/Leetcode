def find_GCD(nums: list[int]):
    """
    Given an integer array nums, return the greatest common divisor of the
    smallest number and largest number in nums.
    The greatest common divisor of two numbers is the largest
    positive integer that evenly divides both numbers.
    """
    min_num, max_num = min(nums), max(nums)

    def helper(x: int, y: int):
        if y == 0:
            return abs(x)
        return helper(y, x % y)
    return helper(min_num, max_num)


print(find_GCD([2, 5, 6, 9, 10]))
print(find_GCD([7, 5, 6, 8, 3]))