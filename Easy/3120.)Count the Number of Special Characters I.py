def number_of_special_chars(word: str):
    """
    You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

    Return the number of special letters in word.
    """
    counter = 0
    special = set()
    for char in word:
        if char.upper() in word and char.lower() in word and char not in special:
            counter += 1
            special.add(char.lower())
            special.add(char.upper())
    return counter


print(number_of_special_chars("aaAbcBC"))
print(number_of_special_chars("abc"))
print(number_of_special_chars("abBCab"))