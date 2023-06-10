def is_valid(s: str):
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    parentheses = {"(": ")", "{": "}", "[": "]"}
    queue = []
    for i in s:
        if i in parentheses:
            queue.append(i)
        else:
            if queue:
                open_parentheses = queue.pop()
                if parentheses[open_parentheses] != i:
                    return False
            else:
                return False
    if queue:
        return False
    return True


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
