def large_group_positions(s: str):
    ans = []
    i = 0
    while i < len(s) - 1:
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        if j - i >= 3:
            ans.append([i, j - 1])
            i = j - 1
        i += 1
    return ans


print(large_group_positions("abbxxxxzzy"))
print(large_group_positions("abc"))
print(large_group_positions("abcdddeeeeaabbbcd"))
print(large_group_positions("aa"))
