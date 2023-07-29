def can_construct(ransom_note: str, magazine: str):
    list_magazine = list(magazine)
    for i in ransom_note:
        if i in list_magazine:
            list_magazine.remove(i)
        else:
            return False
    return True


print(can_construct("a", "b"))
print(can_construct("aa", "ab"))
print(can_construct("aa", "aab"))