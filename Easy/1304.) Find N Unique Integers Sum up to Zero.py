def sum_zero(n: int):
    """
    Given an integer n, return any array containing n unique integers such that they add up to 0.
    """
    ans = []
    if int(n % 2) != 0:
        ans.append(0)
    for i in range(1, n//2 + 1):
        ans.append(i)
        ans.append(-i)
    return ans


print(sum_zero(5))
print(sum_zero(3))
print(sum_zero(1))