def is_palindrome(x: int):
    """
    Given an integer x, return true if x is a palindrome and false otherwise.
    """
    return str(x)[::-1] == str(x)


def is_palindrome_second(x: int):
    if x < 0:
        return False
    original_number = x
    new_number = 0
    while x:
        x, digit = divmod(x, 10)
        new_number = new_number * 10 + digit
    return new_number == original_number


print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))

print(is_palindrome_second(121))
print(is_palindrome_second(-121))
print(is_palindrome_second(10))