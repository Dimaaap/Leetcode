def is_valid(s: str) -> bool:
    open_chars = ["(", "[", "{"]
    valid_chars = {"(": ")", "[": "]", "{": "}"}
    stack = []
    i = 0

    while i < len(s):
        if not stack:
            if s[i] not in open_chars:
                return False
            else:
                stack.append(s[i])
                i += 1
                continue
        if s[i] in open_chars:
            stack.append(s[i])
            i += 1
            continue
        else:
            last_char = stack[-1]
            if valid_chars[last_char] != s[i]:
                return False
            else:
                stack.pop()
        i += 1
    if stack:
        return False
    return True


print(is_valid("()"))
print(is_valid("([{}])"))
print(is_valid("[(])"))