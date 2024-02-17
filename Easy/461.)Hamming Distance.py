def hamming_distance(x: int, y: int):
    ans = 0
    while x or y:
        ans += (x & 1) != (y & 1)
        x >>= 1
        y >>= 1
    return ans


print(hamming_distance(1, 4))
print(hamming_distance(3, 1))