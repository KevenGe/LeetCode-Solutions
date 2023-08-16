# 面试题 02.08. 环路检测
# https://leetcode-cn.com/problems/linked-list-cycle-lcci/

################################################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None

        low = head
        fast = head.next

        while low is not fast:
            low = low.next

            if fast.next is None or fast.next.next is None:
                return None
            fast = fast.next.next

        low = head
        fast = fast.next

        while low is not fast:
            low = low.next
            fast = fast.next

        return low


################################################################################


if __name__ == '__main__':
    solution = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n2

    print(solution.detectCycle(n1).val)
