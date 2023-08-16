# 剑指 Offer 24. 反转链表【待完成】
# https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/9pdjbm/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head is None:
#             return None

#         newHead = head
#         head = head.next

#         while head is not None:
#             tmp = head
#             head = head.next

#             tmp.next = newHead
#             newHead = tmp

#         return newHead


# if __name__ == "__main__":
#     so = Solution()

#     a = ListNode(1)
#     b = ListNode(2)
#     c = ListNode(3)
#     a.next = b
#     b.next = c

#     print(so.reverseList(a))
