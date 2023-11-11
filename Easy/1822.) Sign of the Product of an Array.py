def array_sign(nums: list[int]):
    """
    There is a function signFunc(x) that returns:
        1 if x is positive.
        -1 if x is negative.
        0 if x is equal to 0.
    You are given an integer array nums. Let product be the product of all values in the array nums.
    Return signFunc(product).
    """
    product = 1
    for i in nums:
        product *= i
    if product > 0:
        return 1
    return -1 if product < 0 else 0


print(array_sign([-1, -2, -3, -4, 3, 2, 1]))
print(array_sign([1, 5, 0, 2, -3]))
print(array_sign([-1, 1, -1, 1, -1]))


