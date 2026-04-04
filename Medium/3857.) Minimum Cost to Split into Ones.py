def min_cost(n: int) -> int:
    """
    You are given an integer n.
    In one operation, you may split an integer x into two positive integers a and b such that a + b = x.
    The cost of this operation is a * b.
    Return an integer denoting the minimum total cost required to split the integer n into n ones.
    """

    total_cost = 0

    while n > 1:
        min_part = 1
        other_part = n - 1
        cost = min_part * other_part
        total_cost += cost
        n = other_part

    return total_cost


print(min_cost(3))
print(min_cost(4))