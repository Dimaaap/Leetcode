def count_digit_occurrences(nums: list[int], digit: int) -> int:
    """
    You are given an integer array nums and an integer digit.
    Return the total number of times digit appears in the decimal representation of all elements in nums.
    """

    digits = "".join([str(digit) for digit in nums])

    return digits.count(str(digit))


print(count_digit_occurrences([12, 54, 32, 22], 2))
print(count_digit_occurrences([1, 34, 7], 9))