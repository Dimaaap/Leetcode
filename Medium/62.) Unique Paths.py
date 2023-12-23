from functools import lru_cache


@lru_cache(None)
def unique_paths(m: int, n: int):
    if m == 1 or n == 1:
        return 1
    return unique_paths(m, n - 1) + unique_paths(m - 1, n)


print(unique_paths(3, 7))
print(unique_paths(3, 2))