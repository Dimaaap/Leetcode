def residue_prefixes(s: str) -> int:
    """
    You are given a string s consisting only of lowercase English letters.
    A prefix of s is called a residue if the number of distinct characters in the prefix is equal to len(prefix) % 3.
    Return the count of residue prefixes in s.
    A prefix of a string is a non-empty substring that starts from the beginning of the string and extends to
    any point within it.
    """

    i = 0
    count = 0
    while i < len(s):
        prefix = s[:i+1]
        distinct_chars = len(set(prefix))
        if distinct_chars == len(prefix) % 3:
            count += 1
        i += 1
    return count


print(residue_prefixes("abc"))
print(residue_prefixes("dd"))
print(residue_prefixes("bob"))
