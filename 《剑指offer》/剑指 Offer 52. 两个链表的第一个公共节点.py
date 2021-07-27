# 剑指 Offer 52. 两个链表的第一个公共节点
# https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/

# TODO: 此题未做出来。题解中，不明白为什么存在None的情况，待解决。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        a = headA
        b = headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a


if __name__ == "__main__":
    solution = Solution()
    # print(solution.getIntersectionNode([2, 6, 4], [1, 5]))
