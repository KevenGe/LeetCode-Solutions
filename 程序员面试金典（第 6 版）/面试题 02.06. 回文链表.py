# 面试题 02.06. 回文链表
# https://leetcode-cn.com/problems/palindrome-linked-list-lcci/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        elif head.next is None:
            return True
        elif head.next.next is None:
            return head.val == head.next.val

        m = head
        r = head

        isOdd = False

        while r is not None:
            r = r.next
            if r is None:
                isOdd = True
                break
            r = r.next
            m = m.next

        lnode = m
        rnode = m.next

        las_head = head
        rev_head = head.next
        while True:
            if rev_head is not lnode:
                t = rev_head.next
                rev_head.next = las_head
                las_head = rev_head
                rev_head = t
            else:
                if isOdd:
                    rnode = lnode.next
                    lnode = las_head
                else:
                    rnode = lnode
                    lnode = las_head
                break

        while lnode is not None and rnode is not None:
            if lnode.val != rnode.val:
                return False
            lnode = lnode.next
            rnode = rnode.next
        return True


if __name__ == '__main__':
    solution = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(2)
    n4 = ListNode(1)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    print(solution.isPalindrome(n1))


