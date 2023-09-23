def count_words(words1: list[str], words2: list[str]):
    """
    Given two string arrays words1 and words2, return the number of strings that
    appear exactly once in each of the two arrays.
    """
    intersection_words = set(words1) & set(words2)
    counter = 0
    for i in intersection_words:
        if words1.count(i) == 1 and words2.count(i) == 1:
            counter += 1
    return counter


print(count_words(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]))
print(count_words(["b", "bb", "bbb"], ["a", "aa", "aaa"]))
print(count_words(["a", "ab"], ["a", "a", "a", "ab"]))
