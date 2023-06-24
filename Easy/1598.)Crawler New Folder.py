def min_operators(logs: list[str]):
    deep = 0
    for dir_folder in logs:
        if dir_folder == '../':
            deep -= 1
        elif dir_folder == './':
            continue
        else:
            deep += 1
    return deep


print(min_operators(['d1/', 'd2/', '../', 'd31', './']))
print(min_operators(['d1/', 'd2/', './', 'd3/', '../', 'd31']))