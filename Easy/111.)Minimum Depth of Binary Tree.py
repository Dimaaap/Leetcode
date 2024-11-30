from collections import deque

def min_depth(root) -> int:
    """
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

    Note: A leaf is a node with no children.
    """
    if not root:
        return 0
    q = deque([root])
    ans = 0

    while q:
        ans += 1
        for _ in range(len(q)):
            node = q.popleft()
            if not node.left and not node.right:
                return ans
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)