def count_good_rectangles(rectangles: list[list[int]]):
    """
    You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and
    width wi.
    You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example,
    if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.
    Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.
    Return the number of rectangles that can make a square with a side length of maxLen.
    """
    squares_side = []
    for i, j in rectangles:
        squares_side.append(min(i, j))
    max_square = max(squares_side)
    return squares_side.count(max_square)


print(count_good_rectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
print(count_good_rectangles([[2, 3], [3, 7], [4, 3], [3, 7]]))
print(count_good_rectangles([[5, 8], [3, 9], [3, 12]]))
