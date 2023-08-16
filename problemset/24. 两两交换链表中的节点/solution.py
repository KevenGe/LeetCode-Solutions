# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        t = head.next
        head.next = t.next
        t.next = head
        
        head.next = self.swapPairs(head.next)
        
        return t

