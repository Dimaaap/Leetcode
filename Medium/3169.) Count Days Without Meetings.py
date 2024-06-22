def count_days(days: int, meetings: list[list[int]]) -> int:
    meetings.sort(key=lambda x: x[0])
    count = abs(meetings[0][0] - 1)
    n = len(meetings)
    for i in range(1, n):
        if meetings[i][0] <= meetings[i - 1][1]:
            if meetings[i][1] < meetings[i - 1][1]:
                meetings[i][1] = meetings[i - 1][1]
        else:
            dy = meetings[i][0] - meetings[i - 1][1]
            count += dy - 1
    count += abs(meetings[n - 1][1] - days)
    return count



print(count_days(10, [[5, 7], [1, 3], [9, 10]]))
print(count_days(5, [[2, 4], [1, 3]]))