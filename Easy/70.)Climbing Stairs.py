def climb_stairs(n: int):
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct
    ways can you climb to the top?
    """
    stairs = [1, 2]
    for i in range(2, n):
        stairs.append(stairs[i - 1] + stairs[i - 2])
    return stairs[n - 1]

