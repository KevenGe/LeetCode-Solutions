# 1. 两数之和
# https://leetcode-cn.com/problems/two-sum/

################################################################################
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


################################################################################

if __name__ == "__main__":
    solution = Solution()
