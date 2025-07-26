def processStr(s: str) -> str:
    """
    You are given a string s consisting of lowercase English letters and the special
    characters: *, #, and %.

    Build a new string result by processing s according to the following rules from left to right:

        If the letter is a lowercase English letter append it to result.
        A '*' removes the last character from result, if it exists.
        A '#' duplicates the current result and appends it to itself.
        A '%' reverses the current result.

    Return the final string result after processing all characters in s.
    """
    stack = []

    for char in s:
        if char.isalpha():
            stack.append(char)
        elif char == "*":
            if stack:
                stack = stack[:-1]
        elif char == "#":
            stack += stack[::]
        else:
            stack = stack[::-1]
    return "".join(stack)


print(processStr("a#b%*"))
print(processStr("z*#"))