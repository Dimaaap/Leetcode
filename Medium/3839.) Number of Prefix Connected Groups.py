from collections import defaultdict


def prefix_connected(words: list[str], k: int) -> int:
    """
    You are given an array of strings words and an integer k.
    Two words a and b at distinct indices are prefix-connected if a[0..k-1] == b[0..k-1].
    A connected group is a set of words such that each pair of words is prefix-connected.
    Return the number of connected groups that contain at least two words, formed from the given words.

    Note:
    Words with length less than k cannot join any group and are ignored.
    Duplicate strings are treated as separate words.

    """

    prefix_count = defaultdict(int)

    for word in words:
        if len(word) >= k:
            prefix = word[:k]
            prefix_count[prefix] += 1
    groups = 0
    for count in prefix_count.values():
        if count >= 2:
            groups += 1
    return groups


print(prefix_connected(["apple", "apply", "banana", "bandit"], 2))
print(prefix_connected(["car", "cat", "cartoon"], 3))
print(prefix_connected(["bat", "dog", "doggy", "bat"], 3))
print(prefix_connected(["bat", "dog", "dog", "doggy", "bat"], 3))