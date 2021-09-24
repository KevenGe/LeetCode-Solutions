# 430. 扁平化多级双向链表
# https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/

################################################################################

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: "Node") -> "Node":
        if head is None:
            return None

        t = head
        while t is not None:
            if t.child is not None:
                t2 = t.next
                t3 = self.flatten(t.child)

                t.next = t3
                t.child = None
                t3.prev = t

                while t3.next is not None:
                    t3 = t3.next

                t3.next = t2
                if t2 is not None:
                    t2.prev = t3
            t = t.next

        return head


################################################################################

if __name__ == "__main__":
    solution = Solution()
