# 61. 旋转链表
# https://leetcode-cn.com/problems/rotate-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k: int):
        if head is None:
            return None

        tail = head
        count = 1
        while tail.next is not None:
            tail = tail.next
            count += 1

        k = k % count
        k = count - k

        if k == 0:
            return head

        mid = head
        k -= 1
        while k != 0:
            k -= 1
            mid = mid.next
        
        tail.next = head
        head = mid.next
        mid.next = None
        return head


if __name__ == "__main__":
    solution = Solution()
