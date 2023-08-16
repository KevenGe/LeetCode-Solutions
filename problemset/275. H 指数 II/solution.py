# 275. H 指数 II
# https://leetcode-cn.com/problems/h-index-ii/

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i = -1
        n = 1
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] >= n:
                n += 1
            else:
                break
        return n - 1


if __name__ == "__main__":
    so = Solution()
