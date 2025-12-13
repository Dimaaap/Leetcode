def total_waviness(num1: int, num2: int) -> int:
    """
    You are given two integers num1 and num2 representing an inclusive range [num1, num2].
    The waviness of a number is defined as the total count of its peaks and valleys:
    A digit is a peak if it is strictly greater than both of its immediate neighbors.
    A digit is a valley if it is strictly less than both of its immediate neighbors.
    The first and last digits of a number cannot be peaks or valleys.
    Any number with fewer than 3 digits has a waviness of 0.
    Return the total sum of waviness for all numbers in the range [num1, num2].
    """

    total = 0

    for i in range(num1, num2 + 1):
        i = str(i)

        if len(i) < 3:
            continue

        for j in range(1, len(i)-1):
            if i[j - 1] < i[j] > i[j + 1]:
                total += 1
            elif i[j - 1] > i[j] < i[j + 1]:
                total += 1
    return total


print(total_waviness(120, 130))
print(total_waviness(198, 202))
print(total_waviness(4848, 4848 ))
