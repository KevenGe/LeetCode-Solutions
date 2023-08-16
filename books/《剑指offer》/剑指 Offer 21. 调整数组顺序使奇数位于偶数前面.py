# 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
# https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            while nums[l] % 2 == 1 and l < r:
                l += 1
            while nums[r] % 2 == 0 and l < r:
                r -= 1
            if l < r:
                t = nums[l]
                nums[l] = nums[r]
                nums[r] = t
        return nums


if __name__ == "__main__":
    solution = Solution()
