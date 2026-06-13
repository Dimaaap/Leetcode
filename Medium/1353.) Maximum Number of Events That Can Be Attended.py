import heapq


def max_events(events: list[list[int]]) -> int:
    """
    You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi
    and ends at endDayi.
    You can attend an event i at any day d where startDayi <= d <= endDayi. You can only attend one event at any time d.
    Return the maximum number of events you can attend.
    """

    events.sort()

    heap = []
    i = 0
    count = 0
    n = len(events)
    day = events[0][0]

    while i < n or heap:
        if not heap:
            day = max(day, events[i][0])
        while i < n and events[i][0] <= day:
            heapq.heappush(heap, events[i][1])
            i += 1

        while heap and heap[0] < day:
            heapq.heappop(heap)

        if heap:
            heapq.heappop(heap)
            count += 1
            day += 1
        else:
            if i < n:
                day = events[i][0]

    return count




print(max_events([[1, 2], [2, 3], [3, 4]]))
print(max_events([[1, 2], [2, 3], [3, 4], [1, 2]]))
print(max_events([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]))
print(max_events([[1, 2], [2, 2], [3, 3], [3, 4], [3, 4]]))