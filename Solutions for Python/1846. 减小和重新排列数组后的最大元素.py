# 1846. 减小和重新排列数组后的最大元素
# https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging/

from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
        return arr[len(arr) - 1]

if __name__ == "__main__":
    so = Solution()
