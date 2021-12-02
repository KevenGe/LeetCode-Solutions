# 面试题 02.05. 链表求和
# https://leetcode-cn.com/problems/sum-lists-lcci/

################################################################################


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        ans = ListNode(0)
        ans_end = ans
        while l1 is not None and l2 is not None:
            tmp_val = l1.val + l2.val + add
            add = tmp_val // 10
            tmp_val = tmp_val % 10

            tmp_listNode = ListNode(tmp_val)
            ans_end.next = tmp_listNode
            ans_end = ans_end.next

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            tmp_val = l1.val + add
            add = tmp_val // 10
            tmp_val = tmp_val % 10

            tmp_listNode = ListNode(tmp_val)
            ans_end.next = tmp_listNode
            ans_end = tmp_listNode

            l1 = l1.next

        while l2 is not None:
            tmp_val = l2.val + add
            add = tmp_val // 10
            tmp_val = tmp_val % 10

            tmp_listNode = ListNode(tmp_val)
            ans_end.next = tmp_listNode
            ans_end = tmp_listNode

            l2 = l2.next

        if add == 1:
            tmp_listNode = ListNode(1)
            ans_end.next = tmp_listNode

        ans = ans.next
        return ans

################################################################################

if __name__ == "__main__":

    n11 = ListNode(4)
    n12 = ListNode(3)
    n21 = ListNode(6)
    n22 = ListNode(4)
    n11.next = n12
    n21.next = n22

    solution = Solution()
    solution.addTwoNumbers(n11, n21)
