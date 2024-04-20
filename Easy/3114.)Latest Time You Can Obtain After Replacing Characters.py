def find_latest_time(s: str):
    s = list(s)
    if s[0] == '?':
        s[0] = '1' if s[1] == '?' or s[1] <= '1' else '0'
    if s[1] == '?':
        s[1] = '1' if s[0] == '1' else '9'
    if s[3] == '?': s[3] = '5'
    if s[4] == '?': s[4] = '9'
    return ''.join(s)



print(find_latest_time("1?:?4"))
print(find_latest_time("0?:5?"))
