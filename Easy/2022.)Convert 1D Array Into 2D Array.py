def construct_2d_array(original: list[int], m: int, n: int) -> list[list[int]]:
    if m * n != len(original):
        return []
    ans = []
    while m:
        tmp = []
        for i in range(n):
            tmp.append(original[0])
            original = original[1:]
        m -= 1
        ans.append(tmp)
    return ans


print(construct_2d_array([1, 2, 3, 4], 2, 2))
print(construct_2d_array([1, 2, 3], 1, 3))
print(construct_2d_array([1, 2], 1, 1))


