from collections import Counter

def find_x_sum(nums: list[int], k: int, x: int) -> list[int]:
    """
    You are given an array nums of n integers and two integers k and x.

    The x-sum of an array is calculated by the following procedure:

    Count the occurrences of all elements in the array.
    Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences,
    the element with the bigger value is considered more frequent.
    Calculate the sum of the resulting array.
    Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

    Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
    """

    def x_sum(nums_list: list[int]):
        ans = 0
        nums_list_counter = Counter(sorted(nums_list)[::-1])
        most_commons_elements = nums_list_counter.most_common(x)
        for num, production in most_commons_elements:
            num_production = num * production
            ans += num_production
        return ans

    res = []
    for i in range(len(nums)):
        sub_list = nums[i: k + i]
        if len(sub_list) == k:
            res.append(x_sum(sub_list))
    return res


print(find_x_sum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2))
print(find_x_sum([3, 8, 7, 8, 7, 5], 2, 2))