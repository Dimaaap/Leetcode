class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def swap_pairs(head):
    dummy = ListNode(val=0)
    dummy.next = head
    prev = dummy
    cur = head
    while cur and cur.next:
        nxt = cur.next
        prev.next = nxt
        cur.next = nxt.next
        nxt.next = cur
        prev = cur
        cur = cur.next
    return dummy.next
