# 面试题 02.02. 返回倒数第 k 个节点
# https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/


################################################################################

from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        que = deque(maxlen=k)

        while head:
            que.append(head.val)
            head = head.next

        return que.popleft()

################################################################################
