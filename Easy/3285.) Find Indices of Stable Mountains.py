def stable_mountains(height: list[int], threshold: int) -> list[int]:
    res = []
    for i in range(1, len(height)):
        if height[i - 1] > threshold:
            res.append(i)
    return res


print(stable_mountains([1, 2, 3, 4, 5], 2))
print(stable_mountains([10, 1, 10, 1, 10], 3))
print(stable_mountains([10, 1, 10, 1, 10], 10))