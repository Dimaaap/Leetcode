def height_checker(heights: list[int]):
    sorted_heights = sorted(heights)
    counter = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            counter += 1
    return counter


print(height_checker([1, 1, 4, 2, 1, 3]))
print(height_checker([5, 1, 2, 3, 4]))
print(height_checker([1, 2, 3, 4, 5]))
