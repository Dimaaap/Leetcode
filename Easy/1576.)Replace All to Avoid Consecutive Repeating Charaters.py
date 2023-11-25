from string import ascii_lowercase
from random import choice


def modify_string(s: str):
    letters = set(ascii_lowercase)
    s = list(s)
    if s[0] == "?":
        s[0] = choice(list(letters - {s[1]}))
    if s[-1] == "?":
        s[-1] = choice(list(letters - {s[-2]}))
    for i in range(1, len(s)-1):
        if s[i] == "?":
            letter = choice(list(letters - {s[i-1], s[i+1]}))
            s[i] = letter
    return ''.join(s)


print(modify_string("?zs"))
print(modify_string("ubv?w"))