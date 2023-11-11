def square_is_white(coordinates: str):
    """
    You are given coordinates, a string that represents the coordinates of a square of the chessboard.
    Return true if the square is white, and false if the square is black.
    The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first,
    and the number second.
    """
    even_white = ("a", "c", "e", "g")
    if coordinates[0] in even_white:
        if int(coordinates[1]) % 2 == 0:
            return True
    else:
        if int(coordinates[1]) % 2 != 0:
            return True
    return False


print(square_is_white("a1"))
print(square_is_white("h3"))
print(square_is_white("c7"))