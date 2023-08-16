# 725. 分隔链表
# https://leetcode-cn.com/problems/split-linked-list-in-parts/

################################################################################

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:

        n = 0
        t = head
        while t is not None:
            t = t.next
            n += 1

        basic, bigNum = divmod(n, k)

        ans = []

        t = head
        for i in range(k):

            num = basic
            if bigNum > 0:
                bigNum -= 1
                num += 1

            if num == 0:
                ans.append(None)
            else:
                t1 = t
                while t1 is not None and num > 1:
                    t1 = t1.next
                    num -= 1
                ans.append(t)
                t = t1.next
                t1.next = None

        return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
