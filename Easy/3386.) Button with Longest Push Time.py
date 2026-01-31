def button_with_longest_push_time(events: list[list[int]]) -> int:
    """
    You are given a 2D array events which represents a sequence of events where a child pushes a series of buttons
    on a keyboard.
    Each events[i] = [indexi, timei] indicates that the button at index indexi was pressed at time timei.
        The array is sorted in increasing order of time.
        The time taken to press a button is the difference in time between consecutive button presses. The time for
        the first button is simply the time at which it was pressed.
    Return the index of the button that took the longest time to push. If multiple buttons have the same longest time,
    return the button with the smallest index.
    """

    res = 0
    res_index = 0

    for index, (key, time) in enumerate(events):
        if index == 0:
            if time > res:
                res = time
                res_index = key
        else:
            pressed_time = time - events[index - 1][1]
            if pressed_time > res:
                res = pressed_time
                res_index = key
            elif pressed_time == res:
                res_index = min(key, res_index)
    return res_index


print(button_with_longest_push_time([[1, 2], [2, 5], [3, 9], [1, 15]]))
print(button_with_longest_push_time([[10, 5], [1, 7]]))
print(button_with_longest_push_time([[9, 4], [19, 5], [2, 8], [3, 11], [2, 15]]))