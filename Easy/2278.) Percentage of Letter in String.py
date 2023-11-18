def percentage_letter(s: str, letter: str):
    """
    Given a string s and a character letter, return the percentage of characters in s that equal letter
    rounded down to the nearest whole percent.
    """
    s_count = s.count(letter)
    return int(s_count / len(s) * 100)


print(percentage_letter("foobar", "o"))
print(percentage_letter("jjjj", "k"))
print(percentage_letter("sgawtb", "s"))