def minimum_cost(cost: list[int]) -> int:
    """
    A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.
    The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or
    equal to the minimum cost of the two candies bought.
    For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3,
    they can take the candy with cost 1 for free, but not the candy with cost 4.
    Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of
    buying all the candies.
    """

    res = 0
    cost = sorted(cost)[::-1]

    if len(cost) < 2:
        return cost[0]

    while len(cost) > 1:
        paid_candies = cost[0] + cost[1]
        cost = cost[3:]
        res += paid_candies

    if cost:
        res += sum(cost)
    return res

print(minimum_cost([1, 2, 3]))
print(minimum_cost([6, 5, 7, 9, 2, 2]))
print(minimum_cost([5, 5]))
print(minimum_cost([3, 3, 3, 1]))