def num_jewels_in_stones(jewels: str, stones: str):
    counter = 0
    jewels_set = set(jewels)
    for stone in stones:
        if stone in jewels_set:
            counter += 1
    return counter


print(num_jewels_in_stones("aA", "aAAbbbb"))
print(num_jewels_in_stones("z", "ZZ"))

