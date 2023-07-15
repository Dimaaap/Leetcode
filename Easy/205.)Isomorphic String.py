def is_isomorphic(s: str, t: str):
    match_dict = {}
    for i in range(len(s)):
        if s[i] in match_dict and match_dict[s[i]] != t[i]:
            return False
        if t[i] in match_dict:
            return False
        match_dict[s[i]] = t[i]
    return True


print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
print(is_isomorphic("paper", "title"))
print(is_isomorphic("badc", "baba"))