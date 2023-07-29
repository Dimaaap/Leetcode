def restore_string(s: str, indices: list[int]):
    result_string = ""
    for index in indices:
        result_string += s[index]
    return result_string


print(restore_string("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
print(restore_string("abc", [0, 1, 2]))