def count_key_changes(s: str):
    counter = 0
    for i in range(1, len(s)):
        if s[i].lower() != s[i-1].lower():
            counter += 1
    return counter


print(count_key_changes("aAbBcC"))
print(count_key_changes("AaaaAaAAaa"))
