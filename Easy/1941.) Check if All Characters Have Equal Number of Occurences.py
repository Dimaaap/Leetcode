def are_occurrences_equal(s: str):
    """
    Given a string s, return true if s is a good string, or false otherwise.
    A string s is good if all the characters that appear in s have the same number of
    occurrences (i.e., the same frequency).
    """
    count_dict = {}
    for char in s:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return len(set(count_dict.values())) == 1


print(are_occurrences_equal("abacbc"))
print(are_occurrences_equal("aaabb"))