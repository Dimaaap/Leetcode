def earliest_time(tasks: list[list[int]]) -> int:
    """
    You are given a 2D integer array tasks where tasks[i] = [si, ti].
    Each [si, ti] in tasks represents a task with start time si that takes ti units of time to finish.
    Return the earliest time at which at least one task is finished.:
    """

    min_time = float("inf")
    for start, end in tasks:
        need_time = start + end
        min_time = min(min_time, need_time)
    return min_time


print(earliest_time([[1, 6], [2, 3]]))
print(earliest_time([[100, 100], [100, 100], [100, 100]]))