def maximum_number_of_string_pairs(words: list[str]) -> int:
    stack = []
    count = 0
    for word in words:
        if word[::-1] not in stack:
            stack.append(word)
        else:
            count += 1
    return count


print(maximum_number_of_string_pairs(["cd", "ac", "dc", "ca", "zz"]))
print(maximum_number_of_string_pairs(["ab", "ba", "cc"]))
print(maximum_number_of_string_pairs(["aa", "ab"]))