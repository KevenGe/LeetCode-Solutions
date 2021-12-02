# 面试题 02.04. 分割链表
# https://leetcode-cn.com/problems/partition-list-lcci/


from itertools import chain


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lt = []
        bt = []

        while head is not None:
            if head.val < x:
                lt.append(head)
            else:
                bt.append(head)
            head = head.next

        ans = None
        ans_end = None
        for t in chain(lt, bt):
            if ans is None:
                ans = t
                ans_end = ans
            else:
                ans_end.next = t
                ans_end = t

        if ans_end is not None:
            ans_end.next = None
        return ans


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    print(solution.partition(node1, 3))
