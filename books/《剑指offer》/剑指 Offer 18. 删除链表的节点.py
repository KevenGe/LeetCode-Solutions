# 剑指 Offer 18. 删除链表的节点
# https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        t = ListNode(-1)
        t.next = head
        t2 = t
        while t.next != None:
            if t.next.val == val:
                t3 = t.next
                t.next = t.next.next
                del t3
                break
            t = t.next
        return t2.next


if __name__ == "__main__":
    solution = Solution()
