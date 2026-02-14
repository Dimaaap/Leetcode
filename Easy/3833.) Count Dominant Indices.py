def dominant_indices(nums: list[int]) -> int:
    """
    You are given an integer array nums of length n.
    An element at index i is called dominant if: nums[i] > average(nums[i + 1], nums[i + 2], ..., nums[n - 1])
    Your task is to count the number of indices i that are dominant.
    The average of a set of numbers is the value obtained by adding all the numbers together and dividing the
    sum by the total number of numbers.
    Note: The rightmost element of any array is not dominant.
    """
    counter = 0

    for i in range(len(nums) - 1):
        current_num = nums[i]

        other_elements = nums[i + 1:]
        average = sum(other_elements) / len(other_elements)
        if current_num > average:
            counter += 1

    return counter


print(dominant_indices([5, 4, 3]))
print(dominant_indices([4, 1, 2]))