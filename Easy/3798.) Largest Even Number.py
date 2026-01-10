def largest_even(s: str) -> str:
    while s:
        int_s = int(s)

        if int_s % 2 == 0:
            return s
        else:
            s = s[:-1]
    return s


print(largest_even("1112"))
print(largest_even("221"))
print(largest_even("1"))
print(largest_even("11"))


