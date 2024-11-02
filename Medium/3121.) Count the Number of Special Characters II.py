def number_of_special_chars(word: str) -> int:
    """
    You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word,
     and every lowercase occurrence of c appears before the first uppercase occurrence of c.

    Return the number of special letters in word.
    """
    counter = 0
    first_last_char = {}

    for index, char in enumerate(word):
        if char.islower():
            first_last_char[char] = index
        else:
            if char in first_last_char:
                continue
            else:
                first_last_char[char] = index

    for char, index in first_last_char.items():
        if char.islower():
            char_upper = char.upper()
            if char_upper in first_last_char and first_last_char[char_upper] > index:
                counter += 1
    return counter


print(number_of_special_chars("aaAbcBC"))
print(number_of_special_chars("abc"))
print(number_of_special_chars("AbBCab"))
print(number_of_special_chars("cCceDC"))