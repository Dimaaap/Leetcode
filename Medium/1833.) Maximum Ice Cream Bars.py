def max_ice_cream(costs: list[int], coins: int) -> int:
    """
    It is a sweltering summer day, and a boy wants to buy some ice cream bars.
    At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the
    price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible.
    Note: The boy can buy the ice cream bars in any order.
    Return the maximum number of ice cream bars the boy can buy with coins coins.
    You must solve the problem by counting sort.
    """

    costs.sort()
    counter = 0

    for cost in costs:
        if coins >= cost:
            coins -= cost
            counter += 1
        else:
            return counter
    return counter


print(max_ice_cream([1, 3, 2, 4, 1], 7))
print(max_ice_cream([10, 6, 8, 7, 7, 8], 5))
print(max_ice_cream([1, 6, 3, 1, 2, 5], 20))
print(max_ice_cream([1, 3, 2, 4, 1], 7))
print(max_ice_cream([11], 10))