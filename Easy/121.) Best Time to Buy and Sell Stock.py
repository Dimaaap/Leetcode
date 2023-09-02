def max_profit(prices: list[int]):
    min_price = float("inf")
    profit = -float("inf")

    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)

    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
