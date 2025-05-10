def furthest_distance_from_origin(moves: str) -> int:
    counter = 0
    first_move = None
    count_l, count_r = moves.count("L"), moves.count("R")
    if count_l >= count_r:
        moves = moves.replace("_", "L")
    else:
        moves = moves.replace("_", "R")
    for move in moves:
        if not counter:
            first_move = move
            counter += 1
        else:
            if move == first_move:
                counter += 1
            else:
                counter -= 1
    return counter


print(furthest_distance_from_origin("L_RL__R"))
print(furthest_distance_from_origin("_R__LL_"))
print(furthest_distance_from_origin("_______"))