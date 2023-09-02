def is_anagram(s: str, t: str):
    list_s = list(s)
    for i in t:
        if i in list_s:
            list_s.remove(i)
        else:
            return False
    return True if not list_s else False


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("ab", "a"))
