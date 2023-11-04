def xor_operation(n: int, start: int):
    xor_list = []
    i = 0
    while i < n:
        xor_list.append(start + 2 * i)
        i += 1
    ans = 0
    for i in range(len(xor_list)):
        ans = ans ^ xor_list[i]
    return ans


print(xor_operation(5, 0))
print(xor_operation(4, 3))
