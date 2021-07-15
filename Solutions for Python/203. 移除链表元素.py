# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        t = head
        while t is not None and t.val == val:
            t = t.next

        if t is None:
            return None

        before = t
        head = t
        t = t.next
        while t is not None:
            if t.val == val:
                before.next = t.next
                t = t.next
            else:
                t = t.next
                before = before.next

        return head
