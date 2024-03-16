from collections import defaultdict

def group_anagrams(strs: list[str]):
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    """
    d = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        d[key].append(s)
    return list(d.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))
