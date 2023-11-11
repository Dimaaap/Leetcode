def check_string(s: str):
    """
    Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears
     before every 'b' in the string. Otherwise, return false.
    """
    stack = []
    for i in s:
        if stack and i == "a" and stack[-1] == "b":
            return False
        stack.append(i)
    return True


print(check_string("aaabbb"))
print(check_string("abab"))
print(check_string("bbb"))