# 930. 和相同的二元子数组
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        right = 0
        left1 = 0
        left2 = 0
        sum1 = 0
        sum2 = 0
        ans = 0
        while right < len(nums):
            sum1 += nums[right]
            while left1 <= right and sum1 > goal:
                sum1 -= nums[left1]
                left1 += 1

            sum2 += nums[right]
            while left2 <= right and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1

            ans += left2 - left1
            right += 1
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
