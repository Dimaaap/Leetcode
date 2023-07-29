def can_place_flowers(flowerbed: list[int], n: int):
    flowerbed = [0] + flowerbed + [0]
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
        if n == 0:
            return True
    return n <= 0


print(can_place_flowers([1, 0, 0, 0, 1], 1))
print(can_place_flowers([1, 0, 0, 0, 1], 2))
print(can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2))
print(can_place_flowers([0, 0, 1, 0, 1], 1))
