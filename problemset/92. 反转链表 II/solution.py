# 92. 反转链表 II
# https://leetcode-cn.com/problems/reverse-linked-list-ii/

import itertools


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        h: ListNode = head

        nhh: ListNode = None
        ntt: ListNode = None
        nh: ListNode = None
        nt: ListNode = None

        # run
        for i in itertools.count(1):
            if left != 1 and i + 1 == left:
                nhh = h
            if i == left:
                nh = h
            if i == right:
                nt = h
            if i == right + 1:
                ntt = h
                break
            h = h.next

        # reversed
        def rev(first: ListNode, last: ListNode):
            end_tmp_node = last.next
            tmp_head = first
            ans_head = None
            while True:
                if ans_head is None:
                    ans_head = tmp_head
                    tmp_head = tmp_head.next
                else:
                    next_tmp_head = tmp_head.next
                    tmp_head.next = ans_head
                    ans_head = tmp_head
                    tmp_head = next_tmp_head
                if tmp_head is end_tmp_node:
                    break
        rev(nh, nt)

        if nhh is None:
            h = nt
            nh.next = ntt
        else:
            h = head
            nhh.next = nt
            nh.next = ntt

        return h


if __name__ == "__main__":

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    solution = Solution()
    print(solution.reverseBetween(node_1, 2, 4))
