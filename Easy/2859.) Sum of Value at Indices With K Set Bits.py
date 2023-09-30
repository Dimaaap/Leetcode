def sum_indices_with_k_set_bits(nums: list[int], k: int):
    """
    You are given a 0-indexed integer array nums and an integer k.
    Return an integer that denotes the sum of elements in nums whose corresponding indices have
    exactly k set bits in their binary representation.
    The set bits in an integer are the 1's present when it is written in binary.
    For example, the binary representation of 21 is 10101, which has 3 set bits.
    """
    ans = 0
    for index in range(len(nums)):
        if str(bin(index)).count("1") == k:
            ans += nums[index]
    return ans


print(sum_indices_with_k_set_bits([5, 10, 1, 5, 2], 1))
print(sum_indices_with_k_set_bits([4, 3, 2, 1], 2))