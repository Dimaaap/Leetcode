def maximum_69_number(num: int):
    num = list(str(num))
    for i in range(len(num)):
        if num[i] == "6":
            num[i] = "9"
            break
    return int(''.join(num))


print(maximum_69_number(9669))
print(maximum_69_number(9996))
print(maximum_69_number(9999))
