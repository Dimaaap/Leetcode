def reverse_words(s: str) -> str:
    """
    You are given a string s consisting of lowercase English words, each separated by a single space.
    Determine how many vowels appear in the first word. Then, reverse each following word that has the same vowel
    count. Leave all remaining words unchanged.
    Return the resulting string.
    Vowels are 'a', 'e', 'i', 'o', and 'u'.
    """
    vowels = "aeiou"
    s = s.split()
    first_word = s[0]
    vowels_count = 0
    for i in first_word:
        if i in vowels:
            vowels_count += 1
    rest_words = s[1:]
    for index, word in enumerate(rest_words):
        word_vowels = 0
        for i in word:
            if i in vowels:
                word_vowels += 1
        if word_vowels == vowels_count:
            word = word[::-1]
            rest_words[index] = word
    res = first_word + ' ' + ' '.join(rest_words)
    return res.strip()


print(reverse_words('cat and mice'))
print(reverse_words('book is nice'))
print(reverse_words('banana healthy'))
print(reverse_words('ten'))
