def make_fancy_string(s: str) -> str:
    """
    A fancy string is a string where no three consecutive characters are equal.
    Given a string s, delete the minimum possible number of characters from s to make it fancy.
    Return the final string after the deletion. It can be shown that the answer will always be unique.
    """
    stack = []
    for letter in s:
        if len(stack) > 1 and letter == stack[-1] == stack[-2]:
            stack.pop()
        stack.append(letter)
    return ''.join(stack)


print(make_fancy_string("leeetcode"))
print(make_fancy_string("aaabaaaa"))
print(make_fancy_string("aab"))
