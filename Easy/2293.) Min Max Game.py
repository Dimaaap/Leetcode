def min_max_game(nums: list[int]):
    """
    You are given a 0-indexed integer array nums whose length is a power of 2.
    Apply the following algorithm on nums:
        1)Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array
        newNums of length n / 2.
        2)For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as
        min(nums[2 * i], nums[2 * i + 1]).
        3)For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as
        max(nums[2 * i], nums[2 * i + 1]).
        4)Replace the array nums with newNums.
        5)Repeat the entire process starting from step 1.
    Return the last number that remains in nums after applying the algorithm.
    """
    while len(nums) > 1:
        find_min = True
        new_num = []
        i = 0
        while i < len(nums):
            if find_min:
                new_num.append(min(nums[i], nums[i+1]))
            else:
                new_num.append(max(nums[i], nums[i+1]))
            i += 2
            find_min = not find_min
        nums = new_num
    return nums[0]


print(min_max_game([1, 3, 5, 2, 4, 8, 2, 2]))
print(min_max_game([3]))

