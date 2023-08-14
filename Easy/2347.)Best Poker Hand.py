def best_hand(ranks: list[int], suits: list[str]):
    if len(set(suits)) == 1:
        return "Flush"
    if any([ranks.count(i) >= 3 for i in ranks]):
        return "Three of a Kind"
    if any([ranks.count(i) >= 2 for i in ranks]):
        return "Pair"
    return "High Card"


print(best_hand([13, 2, 3, 1, 9], ["a", "a", "a", "a", "a"]))
print(best_hand([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"]))
print(best_hand([10, 10, 2, 12, 9], ["a", "b", "c", "a", "d"]))