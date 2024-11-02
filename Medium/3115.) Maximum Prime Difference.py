def maximum_prime_difference(nums: list[int]) -> int:
    """
    You are given an integer array nums.

    Return an integer that is the maximum distance between the indices of two (not necessarily different)
    prime numbers in nums.
    """
    def is_prime(n: int):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    prime_index = []
    for index, num in enumerate(nums):
        if is_prime(num):
            prime_index.append(index)
    min_index, max_index = min(prime_index), max(prime_index)
    return abs(max_index - min_index)


print(maximum_prime_difference([4, 2, 9, 5, 3]))
print(maximum_prime_difference([4, 8, 2, 8]))
print(maximum_prime_difference([1, 7]))