def is_valid_sudoku(board: list[list[str]]) -> bool:
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
    following rules:
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:
        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.
    """

    cells = 9
    lines = []
    cols = []
    for i in range(cells):
        for j in range(cells):
            if board[i][j] != ".":
                lines.append(board[i][j])
            if board[j][i] != ".":
                cols.append(board[j][i])
        if len(set(lines)) < len(lines):
            return False
        if len(set(cols)) < len(cols):
            return False
        lines = []
        cols = []

    for row in range(0, cells, 3):
        for col in range(0, cells, 3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    value = board[row + i][col + j]
                    if value != ".":
                        if value in seen:
                            return False
                        seen.add(value)
    return True


print(is_valid_sudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]))

print(is_valid_sudoku([
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]))