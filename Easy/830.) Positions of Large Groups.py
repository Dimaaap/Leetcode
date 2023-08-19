def large_group_positions(s: str):
    group = []
    result_list = []
    for char in range(len(s) - 1):
        if s[char] == s[char+1]:
            group += s[char]
        else:
            group += s[char]
            if len(group) >= 3:
                result_list.append(group)
            group = ""
    return result_list


print(large_group_positions("abbxxxxxzy"))
print(large_group_positions("abc"))
print(large_group_positions("abcdddeeeeaabbbcd"))