def min_time_to_type(word: str):
    ans = len(word)
    prev = "a"
    for char in word:
        value = (ord(char) - ord(prev)) % 26
        ans += min(value, 26 - value)
        prev = char
    return ans


print(min_time_to_type("abc"))
print(min_time_to_type("bza"))
print(min_time_to_type("zjpc"))