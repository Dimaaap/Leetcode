def product_except_self(nums: list[int]):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
     of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    """
    ans = [1]
    for i in range(1, len(nums)):
        ans.append(ans[-1] * nums[i - 1])
    cur = 1
    for i in range(len(nums) - 2, -1, -1):
        cur *= nums[i + 1]
        ans[i] *= cur
    return ans


print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))
