def max_distance(moves: str) -> int:
    """
    You are given a string moves consisting of the characters 'U', 'D', 'L', 'R', and '_'.
    Starting from the origin (0, 0), each character represents one move on a 2D plane:

    'U': Move up by 1 unit.
    'D': Move down by 1 unit.
    'L': Move left by 1 unit.
    'R': Move right by 1 unit.
    '_': Can be independently replaced with any one of 'U', 'D', 'L', or 'R'.
    Return the maximum Manhattan distance from the origin that can be achieved after all moves have been performed.
    """

    horizontal = "LR"
    vertical = "UD"
    distance = 0
    horizontal_moves = [move for move in moves if move in horizontal]
    distance += abs(horizontal_moves.count("L") - horizontal_moves.count("R"))
    vertical_moves = [move for move in moves if move in vertical]
    distance += abs(vertical_moves.count("U") - vertical_moves.count("D"))
    distance += moves.count("_")

    return distance

print(max_distance("L_D_"))
print(max_distance("U_R"))
print(max_distance("_"))
print(max_distance("UUD_"))
print(max_distance("RUL"))
