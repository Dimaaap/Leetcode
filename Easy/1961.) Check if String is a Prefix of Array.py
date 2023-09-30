def is_prefix_string(s: str, words: list[str]):
    """
    Given a string s and an array of strings words, determine whether s is a prefix string of words.
    A string s is a prefix string of words if s can be made by concatenating the first k strings in
    words for some positive k no larger than words.length.
    Return true if s is a prefix string of words, or false otherwise.
    """
    result = ""
    for word in words:
        result += word
        if result == s:
            return True
    return False


print(is_prefix_string("iloveleetcode", ["i", "love", "leetcode", "apple"]))
print(is_prefix_string("iloveleetcode", ["apples", "i", "love", "leetcode"]))