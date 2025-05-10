from itertools import permutations

def total_numbers(digits: list[int]) -> int:
    """
    You are given an array of digits called digits. Your task is to determine the number of distinct
    three-digit even numbers that can be formed using these digits.
    Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.
    """
    perms = set(permutations(digits, 3))
    counter = 0
    for perm in perms:
        if perm[-1] % 2 == 0 and perm[0] != 0:
            counter += 1
    return counter


print(total_numbers([1, 2, 3, 4]))
print(total_numbers([0, 2, 2]))
print(total_numbers([6, 6, 6]))
print(total_numbers([1, 3, 5]))