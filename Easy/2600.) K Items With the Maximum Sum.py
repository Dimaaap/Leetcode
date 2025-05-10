def k_items_with_maximum_sum(num_ones: int, num_zeroes: int, num_neg_ones: int, k: int) -> int:
    """
    There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.
    You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.
    The bag initially contains:
        numOnes items with 1s written on them.
        numZeroes items with 0s written on them.
        numNegOnes items with -1s written on them.
    We want to pick exactly k items among the available items. Return the maximum possible sum
    of numbers written on the items.
    """
    available_items = [1] * num_ones + [0] * num_zeroes + [-1] * num_neg_ones
    return sum(available_items[:k])


print(k_items_with_maximum_sum(3, 2, 0, 2))
print(k_items_with_maximum_sum(3, 2, 0, 4))