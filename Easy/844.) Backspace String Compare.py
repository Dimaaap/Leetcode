def backspace_compare(s: str, t: str):
    """
    Given two strings s and t, return true if they are equal when both are typed into empty text editors.
    '#' means a backspace character.
    Note that after backspacing an empty text, the text will continue empty.
    """
    stack = []
    for i in s:
        if i != "#":
            stack.append(i)
        else:
            if stack:
                stack.pop()
    t_stack = []
    for i in t:
        if i != "#":
            t_stack.append(i)
        else:
            if t_stack:
                t_stack.pop()
    return stack == t_stack


print(backspace_compare("ab#c", "ad#c"))
print(backspace_compare("ab##", "c#d#"))
print(backspace_compare("a#c", "b"))