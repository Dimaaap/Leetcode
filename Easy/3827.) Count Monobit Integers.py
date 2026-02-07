def count_monobit(n: int) -> int:
    """
    You are given an integer n.
    An integer is called Monobit if all bits in its binary representation are the same.
    Return the count of Monobit integers in the range [0, n] (inclusive).
    """

    counter = 0

    for i in range(0, n + 1):
        bin_form = format(i, "b")
        if len(set(bin_form)) == 1:
            counter += 1
        else:
            continue
    return counter


print(count_monobit(1))
print(count_monobit(4))