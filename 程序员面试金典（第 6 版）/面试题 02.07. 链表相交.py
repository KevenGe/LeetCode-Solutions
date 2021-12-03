# 面试题 02.07. 链表相交
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/

################################################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        l = headA
        r = headB
        l_done = False
        r_done = False

        while True:
            if l is not None and r is not None:
                if l is r:
                    return l

                l = l.next
                if l is None and not l_done:
                    l = headB
                    l_done = True

                r = r.next
                if r is None and not r_done:
                    r = headA
                    r_done = True
            else:
                break

        return None

################################################################################
