def majority_frequency_group(s: str) -> str:
    """
    You are given a string s consisting of lowercase English letters.
    The frequency group for a value k is the set of characters that appear exactly k times in s.
    The majority frequency group is the frequency group that contains the largest number of distinct characters.
    Return a string containing all characters in the majority frequency group, in any order. If two or more frequency
    groups tie for that largest size, pick the group whose frequency k is larger.
    """

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    groups = {}
    for char, count in char_count.items():
        if count in groups:
            groups[count].append(char)
        else:
            groups[count] = [char]
    groups = dict(sorted(groups.items(), key=lambda x: x[0])[::-1])
    max_maj = ""
    for group in groups.values():
        if len(group) > len(max_maj):
            max_maj = group
    return "".join(max_maj)


print(majority_frequency_group("aaabbbccdddde"))
print(majority_frequency_group("abcd"))
print(majority_frequency_group("pfpfgi"))
print(majority_frequency_group("aalbs"))