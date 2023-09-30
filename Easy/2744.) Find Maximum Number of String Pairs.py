def maximum_number_of_string_pairs(words: list[str]):
    """
    You are given a 0-indexed array words consisting of distinct strings.
    The string words[i] can be paired with the string words[j] if:
    The string words[i] is equal to the reversed string of words[j].
    0 <= i < j < words.length.
    Return the maximum number of pairs that can be formed from the array words.
    Note that each string can belong in at most one pair.
    """
    counter = 0
    visited = {}
    for i in words:
        if i not in visited:
            reverse_word = i[::-1]
            visited[reverse_word] = i
        else:
            counter += 1
    return counter


print(maximum_number_of_string_pairs(["cd", "ac", "dc", "ca", "zz"]))
print(maximum_number_of_string_pairs(["ab", "ba", "cc"]))
print(maximum_number_of_string_pairs(["aa", "ab"]))