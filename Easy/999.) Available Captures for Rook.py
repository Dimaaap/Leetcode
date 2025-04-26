def num_rook_captures(board: list[list[str]]) -> int:
    """
    You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R',
    some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

    A rook can move any number of squares horizontally or vertically (up, down, left, right) until it
    reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's
    square in one move.

    Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook
    cannot attack a pawn if there is another piece blocking the path.

    Return the number of pawns the white rook is attacking.
    """
    rook_pos_col = rook_pos_row = None
    counter = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                rook_pos_col = i
                rook_pos_row = j
    i = rook_pos_col - 1
    j = rook_pos_col + 1
    while i > -1 or j < 8:
        if i >= 0 and board[i][rook_pos_row] == "p":
            counter += 1
            i = -1
        elif j < 8 and board[j][rook_pos_row] == "p":
            counter += 1
            j = 8
        elif j < 8 and board[j][rook_pos_row] == "B":
            j = 8
        elif i >= 0 and board[i][rook_pos_row] == "B":
            i = -1
        else:
            i -= 1
            j += 1
    i = rook_pos_row - 1
    j = rook_pos_row + 1
    while i > -1 or j < 8:
        if i >= 0 and board[rook_pos_col][i] == "p" :
            counter += 1
            i = -1
        elif j < 8 and board[rook_pos_col][j] == "p":
            counter += 1
            j = 8
        elif j < 8 and board[rook_pos_col][j] == "B":
            j = 8
        elif i >= 0 and board[rook_pos_col][i] == "B":
            i = -1
        else:
            i -= 1
            j += 1
    return counter


print(num_rook_captures([[".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".","R",".",".",".","p"],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."]]
                        ))

print(num_rook_captures([[".",".",".",".",".",".","."],
                         [".","p","p","p","p","p",".","."],
                         [".","p","p","B","p","p",".","."],
                         [".","p","B","R","B","p",".","."],
                         [".","p","p","B","p","p",".","."],
                         [".","p","p","p","p","p",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."]]
                        ))

print(num_rook_captures([[".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         ["p","p",".","R",".","p","B","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".","B",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".",".",".",".",".","."]]))

print(num_rook_captures([[".",".",".",".",".",".","p","."],
                         ["p",".",".",".",".",".","R","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".","p","."]]))