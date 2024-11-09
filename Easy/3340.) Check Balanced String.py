def is_balanced(num: str) -> bool:
    """
    You are given a string num consisting of only digits. A string of digits is called balanced if
    the sum of the digits at even indices is equal to the sum of digits at odd indices.

    Return true if num is balanced, otherwise return false.
    """
    even_sum = odd_sum = 0

    for index, i in enumerate(num):
        if index % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return even_sum == odd_sum


print(is_balanced("1234"))
print(is_balanced("24123"))