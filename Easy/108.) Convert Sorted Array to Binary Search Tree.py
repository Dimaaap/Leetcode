class TreeNode:
    def __init__(self, value):
        self.value = value


def sorted_array_to_bst(nums: list[int]):
    """
    Given an integer array nums where the elements are sorted in ascending order, convert it to a
    height-balanced binary search tree.
    """
    def rec(nums, start, end):
        if start <= end:
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = rec(nums, start, mid - 1)
            node.right = rec(nums, mid + 1, end)
            return node
    return rec(nums, 0, len(nums) - 1)
