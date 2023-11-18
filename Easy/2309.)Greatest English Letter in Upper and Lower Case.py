def greatest_letter(s: str):
    ans = ""
    for i in s:
        if i.isupper() and i.lower() in s:
            ans = max(i, ans)
        elif i.islower() and i.upper() in s:
            ans = max(i.upper(), ans)
    return ans


print(greatest_letter("lEeTcOdE"))
print(greatest_letter("arRAzFif"))
print(greatest_letter("AbCdEfGhIjK"))