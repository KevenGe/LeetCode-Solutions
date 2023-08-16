# 581. 最短无序连续子数组
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]

        return 0 if right == -1 else right - left + 1


def test_1():
    solution = Solution()
    assert solution.findUnsortedSubarray([2, 3, 3, 2, 4]) == 3


if __name__ == "__main__":
    solution = Solution()
    test_1()
