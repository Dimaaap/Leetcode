def sum_odd_length_subarrays(arr: list[int]):
    """
    Given an array of positive integers arr,
    return the sum of all possible odd-length subarrays of arr.
    """
    total_sum = 0
    odd_len_range_list = list(range(1, len(arr)+1, 2))



print(sum_odd_length_subarrays([1, 4, 2, 5, 3]))