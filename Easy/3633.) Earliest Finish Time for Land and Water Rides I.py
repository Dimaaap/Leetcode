def earliest_finish_time(land_start_time: list[int], land_duration: list[int],
                         water_start_time: list[int], water_duration: list[int]) -> int:
    """
    You are given two categories of theme park attractions: land rides and water rides.
        Land rides
            landStartTime[i] – the earliest time the ith land ride can be boarded.
            landDuration[i] – how long the ith land ride lasts.

        Water rides
            waterStartTime[j] – the earliest time the jth water ride can be boarded.
            waterDuration[j] – how long the jth water ride lasts.

    A tourist must experience exactly one ride from each category, in either order.

    A ride may be started at its opening time or any later moment. If a ride is started at time t, it finishes at
    time t + duration.Immediately after finishing one ride the tourist may board the other (if it is already open)
    or wait until it opens.

    Return the earliest possible time at which the tourist can finish both rides.
    """
    min_finish = float("inf")

    for i in range(len(land_start_time)):
        land_finish_time = land_start_time[i] + land_duration[i]

        for j in range(len(water_start_time)):
            water_start = max(land_finish_time, water_start_time[j])
            finish = water_start + water_duration[j]
            min_finish = min(min_finish, finish)

    for i in range(len(water_start_time)):
        water_finish_time = water_start_time[i] + water_duration[i]

        for j in range(len(land_start_time)):
            land_start = max(water_finish_time, land_start_time[j])
            finish = land_start + land_duration[j]
            min_finish = min(min_finish, finish)

    return min_finish


print(earliest_finish_time([2, 8], [4, 1], [6], [3]))
print(earliest_finish_time([5], [3], [1], [10]))
print(earliest_finish_time([99], [59], [99, 54], [85, 20]))
print(earliest_finish_time([94, 46], [59, 97], [7], [13]))
