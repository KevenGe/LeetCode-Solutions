# 剑指 Offer 35. 复杂链表的复制
# https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if head is None:
            return None

        ht = head

        ans = Node(head.val)
        t = ans
        fn = {ht: t}
        while ht.next != None:
            t.next = Node(ht.next.val)
            t = t.next
            ht = ht.next
            fn[ht] = t

        ht = head
        t = ans
        while ht != None:
            if ht.random != None:
                t.random = fn[ht.random]
            ht = ht.next
            t = t.next
        return ans


if __name__ == "__main__":
    solution = Solution()
