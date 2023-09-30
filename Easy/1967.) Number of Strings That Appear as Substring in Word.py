def num_of_strings(patterns: list[str], word: str):
    return len([i for i in patterns if i in word])


print(num_of_strings(["a", "abc", "bc", "d"], "abc"))
print(num_of_strings(["a", "b", "c"], "aaaabbbbb"))