def count_good_substrings(s: str):
    """
    A string is good if there are no repeated characters.
    Given a string s, return the number of good substrings of length three in s
    Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
    A substring is a contiguous sequence of characters in a string.
    """
    counter = 0
    if len(s) < 3:
        return 0
    first_substring = list(s[:3])
    if len(set(first_substring)) == len(first_substring):
        counter += 1
    for char in s[3:]:
        first_substring.pop(0)
        first_substring.append(char)
        if len(set(first_substring)) == len(first_substring):
            counter += 1
    return counter


print(count_good_substrings("xyzzaz"))
print(count_good_substrings("aababcabc"))

