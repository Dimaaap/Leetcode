def self_dividing_numbers(left: int, right: int):
    """
    A self-dividing number is a number that is divisible by every digit it contains.
    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
    A self-dividing number is not allowed to contain the digit zero.
    Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
    """
    res = []
    for i in range(left, right + 1):
        if is_self_dividing(i):
            res.append(i)
    return res


def is_self_dividing(num: int):
    if "0" in str(num):
        return False
    list_digits = []
    new_num = num
    while num:
        num, rest = divmod(num, 10)
        list_digits.insert(0, rest)
    return all([new_num % i == 0 for i in list_digits])


print(self_dividing_numbers(1, 22))
print(self_dividing_numbers(47, 85))
