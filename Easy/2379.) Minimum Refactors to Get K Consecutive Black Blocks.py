def minimum_recolors(blocks: str, k: int):
    """
    You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B',
    representing the color of the ith block. The characters 'W' and 'B' denote the colors white and
    black, respectively.
    You are also given an integer k, which is the desired number of consecutive black blocks.
    In one operation, you can recolor a white block such that it becomes a black block.
    Return the minimum number of operations needed such that there is at least one occurrence of k
    consecutive black blocks.
    """
    i, j, min_rec = 0, k, k
    while j <= len(blocks):
        sector = blocks[i:j]
        count_w = sector.count('W')
        min_rec = min(min_rec, count_w)
        i += 1
        j += 1
    return min_rec


print(minimum_recolors("WBBWWBBWBW", 7))
print(minimum_recolors("WBWBBBW", 3))