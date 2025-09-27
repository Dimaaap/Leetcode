from collections import Counter


def min_deletions(s: str, k: int) -> int:
    """
    You are given a string s consisting of lowercase English letters, and an integer k.
    Your task is to delete some (possibly none) of the characters in the string so that the number of distinct
    characters in the resulting string is at most k.
    Return the minimum number of deletions required to achieve this.
    """
    most_common = dict(Counter(s).most_common(k))
    total_values = sum(most_common.values())
    return len(s) - total_values


print(min_deletions("abc", 2))
print(min_deletions("aabb", 2))
print(min_deletions("yyyzz", 1))
print(min_deletions("adx", 1))