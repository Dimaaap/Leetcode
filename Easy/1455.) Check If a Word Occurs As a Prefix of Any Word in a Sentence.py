def is_prefix_of_word(sentence: str, search_word: str):
    """
    Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word.
    If searchWord is a prefix of more than one word, return the index of the first word (minimum index).
    If there is no such word return -1.
    A prefix of a string s is any leading contiguous substring of s.
    """
    sentence = sentence.split()
    for index, word in enumerate(sentence):
        if word.startswith(search_word):
            return index + 1
    return -1


print(is_prefix_of_word("i love eating burger", "burg"))
print(is_prefix_of_word("this problem is an easy problem", "pro"))
print(is_prefix_of_word("i am tired", "you"))