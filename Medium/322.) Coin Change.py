def coin_change(coins: list[int], amount: int):
    """
    You are given an integer array coins representing coins of different denominations and an
    integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
    """
    memo = {}

    def helper(amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float("inf")
        if amount in memo:
            return memo[amount]
        ret = float("inf")

        for coin in coins:
            ret = min(ret, 1 + helper(amount - coin))
        memo[amount] = ret
        return ret
    ans = helper(amount)
    return ans if ans != float("inf") else -1


print(coin_change([1, 2, 5], 11))
print(coin_change([1], 0))
print(coin_change([2], 3))