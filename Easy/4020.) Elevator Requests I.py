def elevator_requests(n: int, requests: list[int]) -> int:
    seconds = 0
    start_pos = 0

    for request in requests:
        needed_time = abs(request - start_pos)
        seconds += needed_time
        start_pos = request
    return seconds


print(elevator_requests(5, [2, 1, 4, 3]))
print(elevator_requests(3, [2, 0, 0]))