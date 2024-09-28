def check_valid(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    num_range = set(range(1, n + 1))
    is_good = True
    for i in range(n):
        if not num_range - set(matrix[i]):
            is_good = True
        else:
            return False
    cols = [col for col in zip(*matrix)]
    for col in cols:
        if num_range - set(col):
            return False
    return is_good

print(check_valid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
print(check_valid([[1, 1, 1], [1, 2, 3], [1, 2, 3]]))