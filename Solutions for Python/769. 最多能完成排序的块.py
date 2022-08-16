# 769. 最多能完成排序的块
# https://leetcode.cn/problems/max-chunks-to-make-sorted/

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0

        ri = 0

        for i, a in enumerate(arr):
            if a > ri:
                ri = a

            if i == ri:
                count += 1
                ri = i + 1

        return count


if __name__ == "__main__":
    so = Solution()
    assert so.maxChunksToSorted([4, 3, 2, 1, 0]) == 1
    assert so.maxChunksToSorted([1, 0, 2, 3, 4]) == 4
