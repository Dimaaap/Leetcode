class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def remove_duplicates(self, head):
        if not head:
            return None
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head