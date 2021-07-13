#  Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 哈希表
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         a = set()
#         while True:
#             if head is None:
#                 return False
#             if head in a:
#                 return True
#             a.add(head)
#             head = head.next
#         return False


# 快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        low = head
        fast = head
        while True:
            fast = fast.next
            if fast is None:
                return False 
            fast = fast.next
            if fast is None:
                return False 
            low = low.next
            if fast is low:
                return True
        return False
