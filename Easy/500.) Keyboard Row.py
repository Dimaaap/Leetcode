def find_words(words: list[str]):
    """
    Given an array of strings words, return the words that can be typed using letters
    of the alphabet on only one row of American keyboard like the image below.
    In the American keyboard:
    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".
    """
    ans = []
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for word in words:
        new_word = word.lower()
        for row in rows:
            if all([i in row for i in new_word]):
                ans.append(word)
    return ans


print(find_words(["Hello", "Alaska", "Dad", "Peace"]))
print(find_words(["omk"]))
print(find_words(["adsdf", "sfd"]))
