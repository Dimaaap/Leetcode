from collections import defaultdict


def max_digit_range(nums: list[int]) -> int:
    """
    You are given an integer array nums.

    The digit range of an integer is defined as the difference between its largest digit and smallest digit.

    For example, the digit range of 5724 is 7 - 2 = 5.

    Return the sum of all integers in nums whose digit range is equal to the maximum digit range among all
    integers in the array.
    """
    max_range = 0

    num_range_dict = defaultdict(list)

    for num in nums:
        num = str(num)
        max_digit, min_digit = int(max(num)), int(min(num))
        diff = max_digit - min_digit
        num_range_dict[diff].append(int(num))
        max_range = max(max_range, diff)

    res = 0

    for key, value in num_range_dict.items():
        if key == max_range:
            res = sum(value)
    return res

#
print(max_digit_range([5724, 111, 350]))
print(max_digit_range([90, 900]))
print(max_digit_range([76364,80946,83426,86822,8470,77400,91853,17447,37800,96545,84619,58374,35177,32777,97032,59483,19578,5770,90000,65561,11209,66371,24953,4463,11437,45951,55753,96286,37364,30585,40914,74370,78195,84824,3592,97757,11186,22197,77593,96587,73024,12818,18252,48610,90339,97032,5513,6493]))