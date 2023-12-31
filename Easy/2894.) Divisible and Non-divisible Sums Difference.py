def difference_of_sums(n: int, m: int):
    """
    You are given positive integers n and m.
    Define two integers, num1 and num2, as follows:
        num1: The sum of all integers in the range [1, n] that are not divisible by m.
        num2: The sum of all integers in the range [1, n] that are divisible by m.
    Return the integer num1 - num2.
    """
    num1 = num2 = 0
    for i in range(1, n + 1):
        if i % m == 0:
            num2 += i
        else:
            num1 += i
    return num1 - num2


print(difference_of_sums(10, 3))
print(difference_of_sums(5, 6))
print(difference_of_sums(5, 1))