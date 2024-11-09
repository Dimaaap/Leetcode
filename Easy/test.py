def final_string(s: str) -> str:
    s = list(s)
    res = ""
    for i in range(len(s)):
        if s[i] != "i":
            res += s[i]
        else:
            res = res[::-1]
    return res

print(final_string("string"))
print(final_string("poiinter"))