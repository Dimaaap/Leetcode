def nearest_drone(drones: list[list[int]], target: list[int]) -> int:
    """
    You are given a 2D integer array drones, where drones[i] = [xi, yi, rangei] represents the
    x-coordinate, y-coordinate, and travel range of the ith drone.
    You are also given an integer array target = [tx, ty], representing the coordinates of the target.
    A drone drones[i] can reach the target if the Manhattan distance between its coordinates and the
    target coordinates is less than or equal to its rangei.
    Return the index of the reachable drone with the minimum Manhattan distance to the target. If there is a tie,
    return the smallest index. If no drone can reach the target, return -1.
    """

    min_distance = float('inf')
    res_index = -1

    for index, (x, y, distance) in enumerate(drones):
        dist = abs(x - target[0]) + abs(y - target[1])
        if dist <= distance and dist < min_distance:
            min_distance = dist
            res_index = index
    if res_index < 0:
        return -1
    return res_index


print(nearest_drone([[0, 0, 8], [2, 2, 9]], [3, 4]))
print(nearest_drone([[2, 1, 5], [4, 4, 5], [6, 6, 8]], [5, 5]))
print(nearest_drone([[4, 4, 5]], [8, 6]))

