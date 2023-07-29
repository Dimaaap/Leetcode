def word_pattern(pattern: str, s: str):
    s = s.split()
    if len(pattern) != len(s):
        return False
    return len(set(pattern)) == len(set(s)) == len(set(zip(pattern, s)))


print(word_pattern("abba", "dog cat cat dog"))
print(word_pattern("abba", "dog cat cat fish"))
print(word_pattern("aaaa", "dog cat cat dog"))
print(word_pattern("abba", "dog dog dog dog"))
