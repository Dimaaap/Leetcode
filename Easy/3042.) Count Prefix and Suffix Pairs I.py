def count_prefix_and_suffix_pairs(words: list[str]):
    counter = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if is_prefix_and_suffix(words[i], words[j]):
                counter += 1
    return counter


def is_prefix_and_suffix(str1: str, str2: str):
    return str2.startswith(str1) and str2.endswith(str1)


print(count_prefix_and_suffix_pairs(["a", "aba", "ababa", "aa"]))
print(count_prefix_and_suffix_pairs(["pa", "papa", "ma", "mama"]))
print(count_prefix_and_suffix_pairs(["abab", "ab"]))
