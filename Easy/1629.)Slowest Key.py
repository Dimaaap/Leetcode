def slowest_key(release_times: list[int], key_pressed: str):
    time = {}
    prev = 0
    m = 0
    for i in range(0, len(release_times)):
        a = release_times[i] - prev
        prev = release_times[i]
        m = max(m, a)
        if key_pressed[i] not in time:
            time[key_pressed[i]] = a
        else:
            time[key_pressed[i]] = max(time[key_pressed[i]], a)

    return sorted([k for k, v in sorted(time.items(), reverse=True, key=lambda item: item[1]) if v == m], reverse=True)[
        0]


print(slowest_key([9, 29, 49, 50], "cbcd"))
print(slowest_key([12, 23, 36, 46, 62], "spuda"))
