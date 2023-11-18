def number_of_points(nums: list[list[int]]):
    """
    You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line.
     For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the
     ending point of the ith car.
    Return the number of integer points on the line that are covered with any part of a car.
    """
    ans = set()
    for num in nums:
        for i in range(num[0], num[-1] + 1):
            ans.add(i)
    return len(ans)


print(number_of_points([[3, 6], [1, 5], [4, 7]]))
print(number_of_points([[1, 3], [5, 8]]))