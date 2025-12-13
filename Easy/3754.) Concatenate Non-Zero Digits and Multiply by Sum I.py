def sum_and_multiply(n: int) -> int:
    """
    You are given an integer n.
    Form a new integer x by concatenating all the non-zero digits of n in their original order.
    If there are no non-zero digits, x = 0.
    Let sum be the sum of digits in x.
    Return an integer representing the value of x * sum.
    """
    n = str(n)
    non_zero = "".join([i for i in n if i != "0"]) or "0"
    non_zero_sum = sum([int(i) for i in non_zero])
    return int(non_zero) * int(non_zero_sum)


print(sum_and_multiply(10203004))
print(sum_and_multiply(1000))
print(sum_and_multiply(0))