# 2058. 找出临界点之间的最小和最大距离
# https://leetcode-cn.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

################################################################################
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        nodeBef = head
        nodeCur = head.next
        nodeNex = head.next.next

        minBef = -1
        minCur = 1
        minFir = -1

        ans = [1000000000, -1000000000]

        while nodeNex:
            if (nodeBef.val > nodeCur.val < nodeNex.val) or (
                nodeBef.val < nodeCur.val > nodeNex.val
            ):
                if minFir == -1 or minBef == -1:
                    minBef = minFir = minCur
                else:
                    ans[0] = min(ans[0], minCur - minBef)
                    ans[1] = max(ans[1], minCur - minFir)
                    minBef = minCur
            minCur += 1
            nodeBef, nodeCur, nodeNex = nodeCur, nodeNex, nodeNex.next

        if ans[0] == 1000000000:
            return [-1, -1]
        else:
            return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
