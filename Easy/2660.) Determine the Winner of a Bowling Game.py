def is_winner(player1: list[int], player2: list[int]):
    def helper(arr: list[int]):
        points = 0
        for index, element in enumerate(arr):
            if index == 0:
                points += element
            elif index == 1:
                if arr[index - 1] == 10:
                    points += 2 * element
                else:
                    points += element
            else:
                if arr[index - 1] == 10 or arr[index - 2] == 10:
                    points += 2 * element
                else:
                    points += element
        return points

    first_player_points = helper(player1)
    second_player_points = helper(player2)
    if first_player_points > second_player_points:
        return 1
    elif first_player_points < second_player_points:
        return 2
    return 0


def is_winner2(player1: list[int], player2: list[int]):
    def helper(nums: list[int]):
        res, prev1, prev2 = 0, 0, 0
        for n in nums:
            if prev1 == 10 or prev2 == 10:
                res += 2 * n
            else:
                res += n
            prev2, prev1 = prev1, n
        return res

    pl1 = helper(player1)
    pl2 = helper(player2)
    if pl1 > pl2:
        return 1
    elif pl2 > pl1:
        return 2
    return 0


print(is_winner([4, 10, 7, 9], [6, 5, 2, 3]))
print(is_winner([3, 5, 7, 6], [8, 10, 10, 2]))
print(is_winner([2, 3], [4, 1]))
print(is_winner([5, 6, 1, 10], [5, 1, 10, 5]))
print(is_winner2([4, 10, 7, 9], [6, 5, 2, 3]))
print(is_winner2([3, 5, 7, 6], [8, 10, 10, 2]))
print(is_winner2([2, 3], [4, 1]))
print(is_winner2([5, 6, 1, 10], [5, 1, 10, 5]))
