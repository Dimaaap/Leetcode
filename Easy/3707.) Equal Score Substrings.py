from string import ascii_lowercase

def score_balance(s: str) -> bool:
    """
    You are given a string s consisting of lowercase English letters.
    The score of a string is the sum of the positions of its characters in the alphabet,
    where 'a' = 1, 'b' = 2, ..., 'z' = 26.
    Determine whether there exists an index i such that the string can be split into two non-empty
    substrings s[0..i] and s[(i + 1)..(n - 1)] that have equal scores.
    Return true if such a split exists, otherwise return false.
    """
    letter_char = {l: i for i, l in zip(range(1, 27), ascii_lowercase)}
    i = 0
    while i < len(s):
        left, right = s[:i], s[i:]
        left_sum, right_sum = 0, 0
        for char in left:
            left_sum += letter_char[char]
        for char in right:
            right_sum += letter_char[char]
        if left_sum == right_sum:
            return True
        i += 1
    return False


print(score_balance("adcb"))
print(score_balance("bace"))