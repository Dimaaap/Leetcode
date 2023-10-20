def largest_altitude(gain: list[int]):
    """
    There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
    The biker starts his trip on point 0 with altitude equal 0.
    You are given an integer array gain of length n where gain[i] is the net gain in altitude between points
    i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
    """
    res = 0
    ans = [0]
    for i in gain:
        res = res + i
        ans.append(res)
    return max(ans)


print(largest_altitude([-5, 1, 5, 0, -7]))
print(largest_altitude([-4, -3, -2, -1, 4, 3, 2]))