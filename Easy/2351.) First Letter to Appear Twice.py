def repeated_characters(s: str):
    seen_chars = {}
    for i in s:
        if i not in seen_chars:
            seen_chars[i] = 1
        else:
            return i
    return None


print(repeated_characters("abccbaacz"))
print(repeated_characters("abcdd"))