def find_the_difference(s: str, t: str):
    list_s, list_t = list(s), list(t)
    for i in list_t:
        if i in list_s:
            list_s.remove(i)
        else:
            return i


print(find_the_difference("abcd", "abcde"))
print(find_the_difference("", "y"))
print(find_the_difference("a", "aa"))
