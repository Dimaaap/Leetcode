def max_height_of_triangle(red: int, blue: int) -> int:

    """
    You are given two integers red and blue representing the count of red and blue colored balls.
    You have to arrange these balls to form a triangle such that the 1st row will have 1 ball, the 2nd row
    will have 2 balls, the 3rd row will have 3 balls, and so on.

    All the balls in a particular row should be the same color, and adjacent rows should have different colors.

    Return the maximum height of the triangle that can be achieved.
    """

    def start(first, second):
        n = 1

        while True:
            if n % 2 == 1:
                first -= n
            else:
                second -= n
            if first < 0 or second < 0:
                return n - 1
            if first == 0 and second == 0:
                return n
            n += 1
    return max(start(red, blue), start(blue, red))


print(max_height_of_triangle(2, 4))
print(max_height_of_triangle(2, 1))
print(max_height_of_triangle(1, 1))
print(max_height_of_triangle(10, 1))
print(max_height_of_triangle(2, 4))