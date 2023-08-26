def min_operations(logs: list[str]):
    deep = 0
    go_dict = {"../": -1, "./": 0}
    for log in logs:
        if log == "../" and deep == 0:
            continue
        if log in go_dict:
            deep += go_dict[log]
        else:
            deep += 1
    return deep


print(min_operations(["d1/", "d2/", "../", "d21/", "./"]))
print(min_operations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
print(min_operations(["d1/", "../", "../", "../"]))
