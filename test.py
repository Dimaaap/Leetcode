def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    new_num = x
    palindrome = 0
    while x:
        x, res = divmod(x, 10)
        palindrome = palindrome * 10 + res

    return palindrome == new_num


print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))