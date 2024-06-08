def is_valid(s: str):
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
