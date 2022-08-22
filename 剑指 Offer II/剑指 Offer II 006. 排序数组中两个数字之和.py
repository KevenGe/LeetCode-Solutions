# 剑指 Offer II 006. 排序数组中两个数字之和
# https://leetcode.cn/problems/kLl5u1/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            t = numbers[l] + numbers[r]
            if  t== target:
                return [l, r]
            elif t > target:
                r -= 1
            elif t < target:
                l += 1

        return [-1, -1]


if __name__ == "__main__":
    so = Solution()
    print(so.twoSum([1, 2, 4, 6, 10], 8))
