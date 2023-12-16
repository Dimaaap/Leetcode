def climb_stairs(n: int):
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct
    ways can you climb to the top?
    """
    memo = {}
    return helper(n, memo)


def helper(n, memo):
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
    return memo[n]


print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(44))


