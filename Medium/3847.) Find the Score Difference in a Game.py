def score_difference(nums: list[int]) -> int:
    """
    You are given an integer array nums, where nums[i] represents the points scored in the ith game.
    There are exactly two players. Initially, the first player is active and the second player is inactive.

    The following rules apply sequentially for each game i:
        If nums[i] is odd, the active and inactive players swap roles.
        In every 6th game (that is, game indices 5, 11, 17, ...), the active and inactive players swap roles.
        The active player plays the ith game and gains nums[i] points.

    Return the score difference, defined as the first player's total score minus the second player's total score.
    """

    first_player = second_player = 0
    active = "1"

    for index, num in enumerate(nums):
        if num % 2 != 0:
            active = "2" if active == "1" else "1"
        if (index + 1) % 6 == 0:
            active = "2" if active == "1" else "1"
        if active == "1":
            first_player += num
        else:
            second_player += num
    return first_player - second_player


print(score_difference([1, 2, 3]))
print(score_difference([2, 4, 2, 1, 2, 1]))
print(score_difference([1]))