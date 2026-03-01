def toggle_light_bulbs(bulbs: list[int]) -> list[int]:
    """
    You are given an array bulbs of integers between 1 and 100.
    There are 100 light bulbs numbered from 1 to 100. All of them are switched off initially.
    For each element bulbs[i] in the array bulbs:
        If the bulbs[i]th light bulb is currently off, switch it on.
        Otherwise, switch it off.
    Return the list of integers denoting the light bulbs that are on in the end, sorted in ascending order.
    If no bulb is on, return an empty list.
    """

    on_bulbs = []

    for bulb in bulbs:
        if bulb not in on_bulbs:
            on_bulbs.append(bulb)
        else:
            on_bulbs.remove(bulb)
    return sorted(on_bulbs)


print(toggle_light_bulbs([10, 30, 20, 10]))
print(toggle_light_bulbs([100, 100]))