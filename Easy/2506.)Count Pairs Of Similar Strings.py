def similar_pairs(words: list[str]):
    """
    You are given a 0-indexed string array words.
    Two strings are similar if they consist of the same characters.

    For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
    However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
    Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two
    strings words[i] and words[j] are similar.
    """
    counter = 0
    seen = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and set(words[i]) == set(words[j]) and (j, i) not in seen:
                counter += 1
                seen.append((i, j))
    return counter


print(similar_pairs(["aba", "aabb", "abcd", "bac", "aabc"]))
print(similar_pairs(["aabb", "ab", "ba"]))
print(similar_pairs(["nba", "cba", "dba"]))