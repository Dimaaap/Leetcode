def is_isomorphic(s: str, t: str):
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
print(is_isomorphic("paper", "title"))
print(is_isomorphic("badc", "baba"))