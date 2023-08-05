def max_power(s: str):
    counter = 1
    res = [s[0]]
    max_counter = 1
    for i in range(1, len(s)):
        if s[i] == res[-1]:
            counter += 1
            max_counter = max(max_counter, counter)
        else:
            counter = 1
        res.append(s[i])
    return max_counter


print(max_power("leetcode"))
print(max_power("abbcccddddeeeeedcba"))
print(max_power("j"))
print(max_power("cc"))
