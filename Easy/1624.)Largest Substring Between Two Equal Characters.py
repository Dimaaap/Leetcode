def max_length_between_equal_characters(s: str):
    """
    Given a string s, return the length of the longest substring between two equal characters,
    excluding the two characters. If there is no such substring return -1.
    A substring is a contiguous sequence of characters within a string.
    """
    ans = -1
    seen = {}
    for index, char in enumerate(s):
        if char in seen:
            ans = max(ans, index - seen[char] - 1)
        seen.setdefault(char, index)
    return ans

