def check_prime_frequency(nums: list[int]) -> bool:
    """
    You are given an integer array nums.

    Return true if the frequency of any element of the array is prime, otherwise, return false.

    The frequency of an element x is the number of times it occurs in the array.

    A prime number is a natural number greater than 1 with only two factors, 1 and itself.
    """
    for num in set(nums):
        count = nums.count(num)
        if is_prime(count):
            return True
    return False


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(check_prime_frequency([1, 2, 3, 4, 5, 4]))
print(check_prime_frequency([1, 2, 3, 4, 5]))
print(check_prime_frequency([2, 2, 2, 4, 4]))