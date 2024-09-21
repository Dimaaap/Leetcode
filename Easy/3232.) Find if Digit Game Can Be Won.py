def can_alice_win(nums: list[int]) -> bool:
    """
    You are given an array of positive integers nums.

    Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit
    numbers from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is
    strictly greater than the sum of Bob's numbers.

    Return true if Alice can win this game, otherwise, return false.
    """

    one_digit_number = [i for i in nums if i < 10]
    rest_nums = [i for i in nums if i >= 10]
    return sum(one_digit_number) != sum(rest_nums)


print(can_alice_win([1, 2, 3, 4, 10]))
print(can_alice_win([1, 2, 3, 4, 5, 10]))
print(can_alice_win([5, 5, 5, 25]))