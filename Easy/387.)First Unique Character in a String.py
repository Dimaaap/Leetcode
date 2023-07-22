def first_unique_char(s: str):
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    return -1


print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))