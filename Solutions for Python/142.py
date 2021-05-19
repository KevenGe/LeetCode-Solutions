# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        low = head
        fast = head
        while True:
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if fast is None:
                return None
            low = low.next
            if fast is low:
                break

        p1 = head
        p2 = fast
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next
        return p1
