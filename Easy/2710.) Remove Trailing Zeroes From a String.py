def remove_trailing_zeroes(num: str):
    """
    Given a positive integer num represented as a string, return the integer num
    without trailing zeros as a string.
    """
    return num.rstrip("0")


print(remove_trailing_zeroes("51230100"))
print(remove_trailing_zeroes("123"))