# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        bfA = headA
        bfB = headB
        while headA is not headB:
            headA = headA.next if headA is not None else bfB
            headB = headB.next if headB is not None else bfA

        return headA


if __name__ == "__main__":
    so = Solution()
    print(so.getIntersectionNode([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5]))

