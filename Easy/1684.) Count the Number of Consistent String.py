def count_consistent_strings(allowed: str, words: list[str]):
    """
    You are given a string allowed consisting of distinct characters and an array of strings words.
    A string is consistent if all characters in the string appear in the string allowed.
    Return the number of consistent strings in the array words.
    """
    set_allowed = set(allowed)
    counter = 0
    for word in words:
        if set(word) - set_allowed == set():
            counter += 1
    return counter


print(count_consistent_strings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
print(count_consistent_strings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(count_consistent_strings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
