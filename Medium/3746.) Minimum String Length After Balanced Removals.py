def min_length_after_removals(s: str) -> int:
    """
    You are given a string s consisting only of the characters 'a' and 'b'.
    You are allowed to repeatedly remove any substring where the number of 'a' characters is equal to the
    number of 'b' characters. After each removal, the remaining parts of the string are concatenated
    together without gaps.
    Return an integer denoting the minimum possible length of the string after performing any number of such operations.
    """
    a_count, b_count = s.count('a'), s.count('b')
    return abs(a_count - b_count)



print(min_length_after_removals('aabbab'))
print(min_length_after_removals('aaaa'))
print(min_length_after_removals('aaabb'))
print(min_length_after_removals('baa'))