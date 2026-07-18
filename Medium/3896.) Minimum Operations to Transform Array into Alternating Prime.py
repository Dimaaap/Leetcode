def min_operations(nums: list[int]) -> int:
    """
    You are given an integer array nums.

    An array is considered alternating prime if:

    Elements at even indices (0-based) are prime numbers.
    Elements at odd indices are non-prime numbers.
    In one operation, you may increment any element by 1.

    Return the minimum number of operations required to transform nums into an alternating prime array.

    A prime number is a natural number greater than 1 with only two factors, 1 and itself.
    """

    simple_numbers, next_prime = sieve_of_eratosthenes(max(nums) + 20)
    simple_numbers = set(simple_numbers)
    counter = 0

    for index, num in enumerate(nums):
        if index % 2 == 0:
            if num in simple_numbers:
                continue
            else:
                counter += next_prime[num] - num
        else:
            if num in simple_numbers:
                counter += 2 if num == 2 else 1
    return counter


def sieve_of_eratosthenes(limit: int):
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for index in range(2, int(limit ** 0.5) + 1):
        if is_prime[index]:
            for multiple in range(index * index, limit + 1, index):
                is_prime[multiple] = False

    next_prime = [0] * (limit + 1)
    last_prime = -1

    for i in range(limit, -1, -1):
        if is_prime[i]:
            last_prime = i
        next_prime[i] = last_prime
    return [num for num, prime in enumerate(is_prime) if prime], next_prime


print(min_operations([1, 2, 3, 4]))
print(min_operations([5, 6, 7, 8]))
print(min_operations([4, 4]))