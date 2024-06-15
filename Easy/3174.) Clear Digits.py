def clear_digits(s: str) -> str:
    """
    You are given a string s.
    Your task is to remove all digits by doing this operation repeatedly:
        Delete the first digit and the closest non-digit character to its left.
    Return the resulting string after removing all digits.
    """
    s_list = list(s)
    i = 1
    while i < len(s_list):
        if s_list[i].isdigit():
            s_list.pop(i)
            s_list.pop(i - 1)
            i -= 1
        else:
            i += 1
    return ''.join(s_list)


print(clear_digits("abc"))
print(clear_digits("cb34"))