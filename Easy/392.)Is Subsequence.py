def is_subsequence(s: str, t: str):
    output_list = []
    list_s, list_t = list(s), list(t)
    for i in list_s:
        if i in list_t and list_t.count(i) >= list_s.count(i):
            output_list.append(list_t.index(i))
        else:
            return False
    return output_list == sorted(output_list)


print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))
print(is_subsequence("acb", "ahbgdc"))
print(is_subsequence("aaaaaa", "bbaaa"))

