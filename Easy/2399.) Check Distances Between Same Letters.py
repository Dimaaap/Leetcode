from string import ascii_lowercase


def check_distances(s: str, distances: list[int]):
    """
    You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears
    exactly twice. You are also given a 0-indexed integer array distance of length 26.
    Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
    In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i].
    If the ith letter does not appear in s, then distance[i] can be ignored.
    Return true if s is a well-spaced string, otherwise return false.
    """
    letters = tuple(ascii_lowercase)
    digits = tuple(range(0, 26))
    letter_digit = {l: d for l, d in zip(letters, digits)}
    seen = set()
    for i in range(len(s)):
        if s[i] not in seen:
            letter_position = letter_digit[s[i]]
            letter_distance = distances[letter_position]
            if i + letter_distance + 1 < len(s):
                new_letter_position = s[i + letter_distance + 1]
                if new_letter_position != s[i]:
                    return False
            else:
                return False
            seen.add(s[i])
    return True


def check_distances2(s: str, distances: list[int]):
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = i + 1
        else:
            if distances[ord(s[i]) - ord('a')] != i - d[s[i]]:
                return False
    return True

print(check_distances("abaccb", [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(check_distances("aa", [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
