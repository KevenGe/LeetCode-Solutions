# 剑指 Offer 39. 数组中出现次数超过一半的数字
# https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can = -1
        cou = 0
        for num in nums:
            if cou == 0:
                can = num
            cou += 1 if can == num else -1
        return can


if __name__ == "__main__":
    solution = Solution()
