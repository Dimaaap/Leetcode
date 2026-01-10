def remove_zeroes(n: int) -> int:
    """
    You are given a positive integer n.
    Return the integer obtained by removing all zeros from the decimal representation of n.
    """

    new_s = ""
    for i in str(n):
        if i != "0":
            new_s += i
    return int(new_s)


print(remove_zeroes(1020030))
print(remove_zeroes(1))