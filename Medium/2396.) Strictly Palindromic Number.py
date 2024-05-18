def is_strictly_palindromic(n: int):
    """
    An integer n is strictly palindromic if, for every base b
    between 2 and n - 2 (inclusive), the string representation of the
    integer n in base b is palindromic.
    Given an integer n, return true if n is strictly palindromic and false otherwise.
    A string is palindromic if it reads the same forward and backward.
    """
    def int_2_base(n, b):
        r = ""
        while n > 0:
            r += str(n % b)
            n //= b
        return int(r[-1::-1])
    for i in range(2, n-1):
        if int_2_base(n, i) != n:
            return False
    return True


print(is_strictly_palindromic(9))
print(is_strictly_palindromic(4))