def judge_circle(moves: str):
    move_dict = {"U": 1, "D": -1, "L": 1, "R": -1}
    up_down = 0
    left_right = 0
    for move in moves:
        if move in "UD":
            up_down += move_dict[move]
        else:
            left_right += move_dict[move]
    return up_down == 0 and left_right == 0


print(judge_circle("UD"))
print(judge_circle("LL"))
print(judge_circle("LDRRLRUULR"))
