# 面试题 17.14. 最小K个数
# https://leetcode-cn.com/problems/smallest-k-lcci/

from typing import List
import heapq


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(arr))
        return ans


if __name__ == "__main__":
    solution = Solution()
