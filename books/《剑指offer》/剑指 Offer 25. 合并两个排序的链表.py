# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        t = head

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                t.next = l1
                t = t.next
                l1 = l1.next
            else:
                t.next = l2
                t = t.next
                l2 = l2.next
        
        if l1 is not None:
            t.next = l1
        
        if l2 is not None:
            t.next = l2
        
        return head.next
