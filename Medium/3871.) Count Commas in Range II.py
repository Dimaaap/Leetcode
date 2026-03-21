def count_commas(n: int) -> int:
    """
    You are given an integer n.
    Return the total number of commas used when writing all integers from [1, n] (inclusive)
    in standard number formatting.

    In standard formatting:
        A comma is inserted after every three digits from the right.
        Numbers with fewer than 4 digits contain no commas.
    """

    counter = 0

    k = 1

    while True:
        start = 10 ** (k - 1)
        if start > n:
            break

        end = min(n, 10 ** k - 1)
        count_numbers = end - start + 1
        commas = (k - 1) // 3

        counter += count_numbers * commas
        k += 1

    return counter


print(count_commas(1002))
print(count_commas(998))
print(count_commas(1004590))
print(count_commas(2498915))