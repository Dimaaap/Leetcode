def rearrange_array(nums: list[int]) -> list[int]:
    """
    You are given an integer array nums.
    You start with an empty array ans. Repeat the following operation until nums is empty:
        Identify all distinct values currently present in nums.
        Remove one occurrence of every distinct value currently in nums, and append those values to ans
        in ascending order.
    Return the array ans.
    """

    ans = []

    while nums:
        seen = set()

        i = 0
        temp = []
        while i < len(nums):
            num = nums[i]
            if num not in seen:
                el = nums.pop(i)
                temp.append(el)
                seen.add(el)
            else:
                i += 1
        temp.sort()
        ans.extend(temp)
    return ans

print(rearrange_array([3, 1, 3, 2, 1, 3]))
print(rearrange_array([7, 7, 4, 4, 4]))

