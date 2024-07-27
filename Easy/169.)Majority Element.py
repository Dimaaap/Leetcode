from collections import Counter

def majority_element(nums: list[int]):
    """
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    """
    counter = Counter(nums).most_common(1)
    return counter[0][0]


print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))