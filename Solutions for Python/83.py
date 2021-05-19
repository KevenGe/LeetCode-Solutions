# LeetCode 83

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        curNode = head
        preNode = None
        while curNode is not None and curNode.next is not None:
            preNode = curNode
            curNode = curNode.next

            if curNode is None:
                break

            if curNode.val == preNode.val:
                tmpNode = curNode
                preNode.next = curNode.next
                del tmpNode
                curNode = preNode

        return head
