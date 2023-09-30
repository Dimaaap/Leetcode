def vowel_strings(words: list[str], left: int, right: int):
    """
    You are given a 0-indexed array of string words and two integers left and right.
    A string is called a vowel string if it starts with a vowel character and ends with a vowel
    character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.
    Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].
    """
    vowels = "aeiou"
    counter = 0
    for word in words[left: right+1]:
        if word[0] in vowels and word[-1] in vowels:
            counter += 1
    return counter


print(vowel_strings(["are", "amy", "u"], 0, 2))
print(vowel_strings(["hey", "aeo", "mu", "ooo", "artro"], 1, 4))