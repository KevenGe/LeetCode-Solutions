# 剑指 Offer 42. 连续子数组的最大和
# https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -200
        beforeSum = -200
        for i in range(len(nums)):
            # if beforeSum < 0:
            #     ans = max(ans, nums[i])
            #     beforeSum = nums[i]
            # else:
            #     beforeSum = beforeSum + nums[i]
            #     ans = max(ans, beforeSum)
            
            beforeSum = max(nums[i], beforeSum + nums[i])
            ans = max(ans, beforeSum)

        return ans


if __name__ == "__main__":
    so = Solution()
