# LCP 11. 期望个数统计
# https://leetcode-cn.com/problems/qi-wang-ge-shu-tong-ji/

from typing import List


class Solution:
    def expectNumber(self, scores: List[int]) -> int:
        return (len(set(scores)))


if __name__ == "__main__":
    so = Solution()
    print(so.expectNumber([1,1]))
