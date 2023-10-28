def find_delayed_arrival_time(arrival_time: int, delayed_time: int):
    """
    You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive
    integer delayedTime denoting the amount of delay in hours.
    Return the time when the train will arrive at the station. Note that the time in this problem is in 24-hours format.
    """
    total_time = arrival_time + delayed_time
    if total_time >= 24:
        return total_time - 24
    return total_time


print(find_delayed_arrival_time(15, 5))
print(find_delayed_arrival_time(13, 11))