def alternate_digit_sum(n: int):
    flag = True
    ans = [i for i in str(n)]
    res = 0
    for i in ans:
        if flag:
            res += int(i)
        else:
            res -= int(i)
        flag = not flag
    return res


print(alternate_digit_sum(521))
print(alternate_digit_sum(111))
print(alternate_digit_sum(886996))
