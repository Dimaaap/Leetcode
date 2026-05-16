def traffic_signal(timer: int) -> str:
    """
    You are given an integer timer representing the remaining time (in seconds) on a traffic signal.
    The signal follows these rules:
        If timer == 0, the signal is "Green"
        If timer == 30, the signal is "Orange"
        If 30 < timer <= 90, the signal is "Red"

    Return the current state of the signal. If none of the above conditions are met, return "Invalid".
    """

    res = "Invalid"

    if timer == 0:
        res = "Green"
    if timer == 30:
        res = "Orange"
    if 30 < timer <= 90:
        res = "Red"
    return res


print(traffic_signal(60))
print(traffic_signal(5))
