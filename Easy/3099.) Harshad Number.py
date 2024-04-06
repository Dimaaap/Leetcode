def sum_the_digits_of_harshad_number(x: int):
    """
    An integer divisible by the sum of its digits is said to be a Harshad number.
    You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.
    """

    old_x = x
    ans = 0
    while x:
        x, rest = divmod(x, 10)
        ans += rest
    return ans if old_x % ans == 0 else -1


print(sum_the_digits_of_harshad_number(18))
print(sum_the_digits_of_harshad_number(23))