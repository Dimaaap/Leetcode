def my_sqrt(x: int):
    """
    Given a non-negative integer x, return the square root of x rounded
     down to the nearest integer. The returned integer should be non-negative as well.
    You must not use any built-in exponent function or operator.
    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
    """
    if x == 0:
        return x
    low, high = 1, x
    while low <= high:
        mid = low + (high - low) // 2
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            high = mid - 1
        else:
            low = mid + 1
    return high


print(my_sqrt(4))
print(my_sqrt(8))
print(my_sqrt(3))
print(my_sqrt(2147395599))
