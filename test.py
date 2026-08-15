def maximum_length_substring(s: str) -> int:
    max_len = 0

    for i in range(len(s)):
        stack = [s[i]]
        for j in range(i+1, len(s)):
            if stack.count(s[j]) == 2:
                max_len = max(max_len, len(stack))
                stack = []
                break
            else:
                stack.append(s[j])
        if stack:
            max_len = max(max_len, len(stack))
    return max_len


print(maximum_length_substring("bcbbbcba"))
print(maximum_length_substring("aaaa"))