from collections import defaultdict

def num_equiv_domino_pairs(dominoes: list[list[int]]):
    cache = defaultdict(int)
    for a, b in dominoes:
        pair = (b, a) if a > b else (a, b)
        cache[pair] += 1
    return sum([v * (v - 1) // 2 for v in cache.values() if v > 1])


print(num_equiv_domino_pairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
print(num_equiv_domino_pairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))