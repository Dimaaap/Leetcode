def flipping_and_invert_image(image: list[list[int]]):
    n = len(image)
    m = len(image[0])
    for i in range(n):
        image[i] = image[i][::-1]
        k = 0
        while k < m:
            if image[i][k] == 1:
                image[i][k] = 0
            else:
                image[i][k] = 1
            k += 1
    return image


print(flipping_and_invert_image([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(flipping_and_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))