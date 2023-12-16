def sort_vowels(s: str):
    vowels = "aeiouAEIOU"
    i = 0
    j = len(s) - 1
    s = list(s)
    while i <= j:
        if s[i] in vowels and s[j] in vowels:
            if ord(s[i]) > ord(s[j]):
                s[i], s[j] = s[j], s[i]
            j -= 1
            i += 1
        elif s[i] in vowels and s[j] not in vowels:
            j -= 1
        elif s[i] not in vowels and s[j] in vowels:
            i += 1
        else:
            j -= 1
    return ''.join(s)


print(sort_vowels('lEetcOde'))
print(sort_vowels("lYmph"))
print(sort_vowels("RiQYo"))
