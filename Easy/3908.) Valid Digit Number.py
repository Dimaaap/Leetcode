def valid_digit(n: int, x: int) -> bool:
    """
    You are given an integer n and a digit x.
    A number is considered valid if:
        It contains at least one occurrence of digit x, and
        It does not start with digit x.
        
    Return true if n is valid, otherwise return false.
    """

    n = str(n)

    if str(x) in n and n[0] != str(x):
        return True
    return False


print(valid_digit(101, 0))
print(valid_digit(232, 2))
print(valid_digit(5, 1))