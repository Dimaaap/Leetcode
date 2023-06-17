class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode):
    ans = []
    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            ans.append(node.val)
    helper(root)
    return ans


