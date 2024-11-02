def max_energy_boost(energy_drink_a: list[int], energy_drink_b: list[int]) -> int:
    """
    You are given two integer arrays energyDrinkA and energyDrinkB of the same length n by a futuristic sports
    scientist. These arrays represent the energy boosts per hour provided by two different energy drinks,
    A and B, respectively.

    You want to maximize your total energy boost by drinking one energy drink per hour. However,
    if you want to switch from consuming one energy drink to the other, you need to wait for one
    hour to cleanse your system (meaning you won't get any energy boost in that hour).

    Return the maximum total energy boost you can gain in the next n hours.

    Note that you can start consuming either of the two energy drinks.
    """

    dp = [[0 for j in range(len(energy_drink_a) + 3)] for i in range(2)]

    for i in range(len(energy_drink_a) -1, -1, -1):
        dp[0][i] = energy_drink_a[i] + max(dp[0][i + 1], dp[1][i + 2])
        dp[1][i] = energy_drink_b[i] + max(dp[1][i + 1], dp[0][i + 2])
    return max(dp[0][0], dp[1][0])


print(max_energy_boost([1, 3, 1], [3, 1, 1]))
print(max_energy_boost([4, 1, 1], [1, 1, 3]))


