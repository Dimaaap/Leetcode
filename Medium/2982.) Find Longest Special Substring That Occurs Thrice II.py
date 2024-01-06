from collections import defaultdict


def maximum_length(s: str):
    n = len(s)
    mapping = defaultdict(list)
    l = 0
    while l < n:
        r = l
        while r < n and s[l] == s[r]:
            r += 1
        for i in range(r-l, max(0, r-l-4), -1):
            mapping[s[l]].append(i)
        l = r
    res = -1
    for key in mapping:
        if len(mapping[key]) >= 3:
            res = max(res, sorted(mapping[key])[-3])
    return res


print(maximum_length("aaaa"))
print(maximum_length("abdcef"))
print(maximum_length("abcaba"))