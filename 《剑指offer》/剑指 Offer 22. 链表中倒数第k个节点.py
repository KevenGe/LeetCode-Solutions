# 剑指 Offer 22. 链表中倒数第k个节点
# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        stacks = []
        while head:
            stacks.append(head)
            head = head.next

        for i in range(k-1):
            stacks.pop()
        ans = stacks.pop()
        return ans

if __name__ == "__main__":
    solution = Solution()
