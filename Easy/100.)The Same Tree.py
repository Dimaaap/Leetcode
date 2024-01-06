def is_same_tree(p, q):
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    """
    if not p and not q:
        return True
    if not p or not q or q.val != p.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)