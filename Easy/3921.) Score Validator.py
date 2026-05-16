def score_validator(events: list[str]) -> list[int]:
    """
    You are given a string array events.
    Initially, score = 0 and counter = 0. Each element in events is one of the following:
        "0", "1", "2", "3", "4", "6": Add that value to the total score.
        "W": Increase the counter by 1. No score is added.
        "WD": Add 1 to the total score.
        "NB": Add 1 to the total score.
    Process the array from left to right. Stop processing when either:

        All elements in events have been processed, or
        The counter becomes 10.
    Return an integer array [score, counter], where:

    score is the final total score.
    counter is the final counter value.
    """

    score = counter = 0
    i = 0

    while i < len(events) and counter < 10:
        if events[i].isdigit():
            score += int(events[i])
        elif events[i] == "W":
            counter += 1
        elif events[i] in ("WD", "NB"):
            score += 1
        i += 1
    return [score, counter]


print(score_validator(["1", "4", "W", "6", "WD"]))
print(score_validator(["WD", "NB", "0", "4", "4"]))
print(score_validator(["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]))