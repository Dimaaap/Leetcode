def convert_to_base_7(num: int) -> str:
    """
    Given an integer num, return a string of its base 7 representation.
    """
    if num == 0:
        return "0"

    negative = num < 0
    num = abs(num)
    result = []

    while num > 0:
        result.append(str(num % 7))
        num //= 7

    if negative:
        result.append("-")
    return "".join(result[::-1])

print(convert_to_base_7(100))
print(convert_to_base_7(-7))