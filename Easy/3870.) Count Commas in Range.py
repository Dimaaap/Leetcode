def count_commas(n: int) -> int:
    """
    You are given an integer n.
    Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
    In standard formatting:
        A comma is inserted after every three digits from the right.
        Numbers with fewer than 4 digits contain no commas.
    """
    counter = 0

    for i in range(1_000, n + 1):
        counter += 1

    return counter


print(count_commas(1002))
print(count_commas(998))
print(count_commas(10068))
print(count_commas(100_000))