from string import ascii_lowercase


def freq_alphabets(s: str):
    letters = ascii_lowercase
    char_int_dict = {}
    for i in range(1, 27):
        if i < 10:
            char_int_dict[str(i)] = letters[i - 1]
        else:
            char_int_dict[str(i) + "#"] = letters[i - 1]
    i = 0
    counter = ""
    while i < len(s):
        if "#" in s[i: i + 3]:
            counter += char_int_dict[s[i: i + 3]]
            i += 3
        else:
            counter += char_int_dict[s[i]]
            i += 1
    return counter


print(freq_alphabets("10#11#12"))
print(freq_alphabets("1326#"))
