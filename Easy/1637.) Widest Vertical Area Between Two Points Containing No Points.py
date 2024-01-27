def max_width_of_vertical_area(points: list[list[int]]):
    points = sorted(points)
    ans = 0
    for i in range(1, len(points)):
        ans = max(ans, (points[i][0] - points[i - 1][0]))
    return ans


print(max_width_of_vertical_area([[8, 7], [9, 9], [7, 4], [9, 7]]))
print(max_width_of_vertical_area([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
