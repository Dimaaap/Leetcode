def largest_integer(n: int, s: int) -> int:
    """
    You are given two non-negative integers n and s.
    Return the largest integer that has at most n digits and whose sum of digits is s. If no such integer
    exists, return -1.
    """

    max_value = 10 ** n
    res = float('-inf')

    for i in range(0, max_value):
        str_digit = str(i)
        digit_sum = sum(int(i) for i in str_digit)
        if digit_sum == s:
            res = max(res, i)

    if res == float('-inf'):
        return -1
    return res

print(largest_integer(2, 9))
print(largest_integer(2, 19))
print(largest_integer(5,0))