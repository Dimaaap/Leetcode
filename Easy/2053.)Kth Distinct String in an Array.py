def kth_distinct(arr: list[str], k: int):
    for i in arr:
        if arr.count(i) == 1 and k == 1:
            return i
        if arr.count(i) == 1 and k > 1:
            k -= 1
    return ""


print(kth_distinct(["d", "b", "c", "b", "c", "a"], 2))
print(kth_distinct(["aaa", "aa", "a"], 1))
print(kth_distinct(["a", "b", "a"], 3))