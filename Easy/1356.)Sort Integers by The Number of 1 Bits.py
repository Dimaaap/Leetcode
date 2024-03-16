def sort_by_bits(arr: list[int]):
    """
    You are given an integer array arr. Sort the integers in the array in ascending order
    by the number of 1's in their binary representation and in case of two or more
    integers have the same number of 1's you have to sort them in ascending order.

    Return the array after sorting it.
    """
    arr.sort()
    arr = sorted(arr, key=lambda num: bit_count(num))
    return arr


def bit_count(number):
    return bin(number).count("1")


print(sort_by_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(sort_by_bits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))