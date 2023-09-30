def prefix_count(words: list[str], prefix: str) -> int:
    """
    You are given an array of strings words and a string pref.
    Return the number of strings in words that contain pref as a prefix.
    A prefix of a string s is any leading contiguous substring of s.
    """
    counter = 0
    for word in words:
        if word.startswith(prefix):
            counter += 1
    return counter


print(prefix_count(["pay", "attention", "practice", "attend"], "at"))
print(prefix_count(["leetcode", "win", "loops", "success"], "code"))