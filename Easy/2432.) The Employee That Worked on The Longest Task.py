def hardest_worker(n: int, logs: list[list[int]]):
    timer = 0
    current_time = 0
    ans = 0
    for emp_id, emp_time in logs:
        time = emp_time - timer
        if time > current_time:
            current_time = time
            ans = emp_id
        elif time == current_time:
            ans = min(ans, emp_id)
        timer = emp_time
    return ans


print(hardest_worker(10, [[0, 3], [2, 5], [0, 9], [1, 15]]))
print(hardest_worker(26, [[1, 1], [3, 7], [2, 12], [7, 17]]))
print(hardest_worker(2, [[0, 10], [1, 20]]))
print(hardest_worker(70, [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]]))