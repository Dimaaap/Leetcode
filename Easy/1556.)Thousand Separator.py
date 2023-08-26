def thousand_separator(n: int):
    list_n = list(str(n))
    for i in range(len(list_n)-3, 0, -3):
        list_n.insert(i, ".")
    return "".join(list_n)


print(thousand_separator(987))
print(thousand_separator(1234))


