from heapq import nlargest


def last_stone_weight(stones: list[int]):
    if len(stones) < 2:
        return stones[0]
    n = len(stones)
    while n >= 2:
        two_largest = nlargest(2, stones)
        if two_largest[0] == two_largest[1]:
            stones.remove(two_largest[0])
            stones.remove(two_largest[1])
            n -= 2
        else:
            difference = two_largest[0] - two_largest[1]
            stones.remove(two_largest[1])
            index = stones.index(two_largest[0])
            stones[index] = difference
            n -= 1
    if stones:
        return stones[0]
    return 0


print(last_stone_weight([2, 7, 4, 1, 8, 1]))
print(last_stone_weight([1]))