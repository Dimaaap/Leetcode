def score_of_string(s: str):
    """
    You are given a string s. The score of a string is defined
    as the sum of the absolute difference between the
    ASCII values of adjacent characters.
    Return the score of s.
    """
    counter = 0
    i = 0
    while i < len(s)-1:
        diff = abs(ord(s[i]) - ord(s[i+1]))
        counter += diff
        i += 1
    return counter



print(score_of_string("hello"))
print(score_of_string("zaz"))
