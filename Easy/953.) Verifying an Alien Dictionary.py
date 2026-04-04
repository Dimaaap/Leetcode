def is_alien_sorted(words: list[str], order: str) -> bool:
    """
    In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
    The order of the alphabet is some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only
    if the given words are sorted lexicographically in this alien language.
    """
    true_sorting = sorted(words, key=lambda word: [order.index(c) for c in word])
    return words == true_sorting


print(is_alien_sorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(is_alien_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(is_alien_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))