def check_good_integer(n: int) -> bool:
    """
    You are given a positive integer n.
    Let digitSum be the sum of the digits of n, and let squareSum be the sum of the squares of the digits of n.
    An integer is called good if squareSum - digitSum >= 50.
    Return true if n is good. Otherwise, return false.
    """

    n = str(n)

    digit_sum = square_sum = 0

    for i in n:
        digit_sum += int(i)
        square_sum += int(i) ** 2

    diff = square_sum - digit_sum

    return diff >= 50


print(check_good_integer(1000))
print(check_good_integer(19))