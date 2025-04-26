from itertools import combinations_with_replacement


def num_tile_possibilities(tiles: str) -> int:
    a = combinations_with_replacement(tiles,  len(tiles))
    return [''.join(i) for i in a]


print(num_tile_possibilities("AAB"))