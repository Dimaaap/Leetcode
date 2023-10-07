def string_matching(words: list[str]):
    """
    Given an array of string words, return all strings in words that is a substring of another word.
    You can return the answer in any order.
    A substring is a contiguous sequence of characters within a string
    """
    all_words = ''.join(words)
    ans = [i for i in words if all_words.count(i) >= 2]
    return ans


print(string_matching(["mass", "as", "hero", "superhero"]))
print(string_matching(["leetcode", "et", "code"]))

