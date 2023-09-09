def is_acronym(words: list[str], s: str):
    j = 0
    if len(words) != len(s):
        return False
    for word in words:
        if word[0] != s[j]:
            return False
        j += 1
    return True


print(is_acronym(["alice", "bob", "charlie"], "abc"))
print(is_acronym(["an", "apple"], "a"))