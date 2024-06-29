def slowest_key(releases_times: list[int], keys_pressed: str) -> str:
    max_char = keys_pressed[0]
    max_time = releases_times[0]
    for i in range(1, len(keys_pressed)):
        diff = releases_times[i] - releases_times[i - 1]
        if diff > max_time:
            max_time = diff
            max_char = keys_pressed[i]
        elif diff == max_time:
            max_char = max(max_char, keys_pressed[i])
    return max_char



print(slowest_key([9,29,49,50], "cbcd"))
print(slowest_key([12, 23, 36, 46, 62], "spuda"))
