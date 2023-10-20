def is_path_crossing(path: str):
    """
    Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or
    west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
    Return true if the path crosses itself at any point, that is, if at any time you are on a location you have
    previously visited. Return false otherwise.
    """
    coord_list = [(0, 0)]
    for i in path:
        match i:
            case "N":
                new_value = (coord_list[-1][0] + 1, coord_list[-1][1])
                coord_list.append(new_value)
            case "E":
                new_value = (coord_list[-1][0], coord_list[-1][1] + 1)
                coord_list.append(new_value)
            case "S":
                new_value = (coord_list[-1][0] - 1, coord_list[-1][1])
                coord_list.append(new_value)
            case "W":
                new_value = (coord_list[-1][0], coord_list[-1][-1] - 1)
                coord_list.append(new_value)
    for i in coord_list:
        if coord_list.count(i) > 1:
            return True
    return False


print(is_path_crossing("NES"))
print(is_path_crossing("NESWW"))
