def max_substrings(word: str) -> int:
    """
    You are given a string word.

    Return the maximum number of non-intersecting substrings of word that are at least four characters
    long and start and end with the same letter.
    """

    ans = 0
    first_pos = {}

    for j, char in enumerate(word):
        if char not in first_pos:
            first_pos[char] = j

        if j - first_pos[char] >= 3:
            ans += 1
            first_pos.clear()
    return ans



print(max_substrings("abcdeafdef"))
print(max_substrings("bcdaaaab"))