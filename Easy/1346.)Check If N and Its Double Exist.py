def check_if_exist(arr: list[int]):
    seen = set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i / 2)
        seen.add(i * 2)
    return False


print(check_if_exist([10, 2, 5, 3]))
print(check_if_exist([3, 1, 7, 11]))
print(check_if_exist([7, 1, 14, 11]))