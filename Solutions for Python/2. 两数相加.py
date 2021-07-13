# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        ans = head

        add = 0
        while l1 is not None and l2 is not None:
            t = l1.val + l2.val + add
            add = t // 10
            t = t % 10

            ans.next = ListNode(t)
            ans = ans.next

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            t = l1.val + add
            add = t // 10
            t = t % 10

            ans.next = ListNode(t)
            ans = ans.next

            l1 = l1.next
        

        while l2 is not None:
            t = l2.val + add
            add = t // 10
            t = t % 10

            ans.next = ListNode(t)
            ans = ans.next

            l2 = l2.next
        
        if add != 0:
            ans.next = ListNode(add)
        
        head = head.next
        return head
