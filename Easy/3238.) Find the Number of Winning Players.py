from collections import Counter

def winning_players_count(n: int, pick: list[list[int]]) -> int:
    """
    You are given an integer n representing the number of players in a game and a 2D array pick
    where pick[i] = [xi, yi] represents that the player xi picked a ball of color yi.

    Player i wins the game if they pick strictly more than i balls of the same color. In other words,

        Player 0 wins if they pick any ball.
        Player 1 wins if they pick at least two balls of the same color.
        ...
        Player i wins if they pick at leasti + 1 balls of the same color.

    Return the number of players who win the game.

    Note that multiple players can win the game.
    """
    winners_count = 0
    game_hash = {}
    for (player, choice) in pick:
        if player not in game_hash:
            game_hash[player] = [choice]
        else:
            game_hash[player].append(choice)
    for key, value in game_hash.items():
        game_hash[key] = Counter(value).most_common(1)
    for key, value in game_hash.items():
        if value[0][1] >= key + 1:
            winners_count += 1
    return winners_count


print(winning_players_count(4, [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]))
print(winning_players_count(5, [[1, 1], [1, 2], [1, 3], [1, 4]]))
print(winning_players_count(5, [[1, 1], [2, 4], [2, 4], [2, 4]]))
