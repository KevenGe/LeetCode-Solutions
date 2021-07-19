# 1838. 最高频元素的频数
# https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element/
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        sums = 0
        ans = 1

        right = 1
        while right < len(nums):
            sums += (right - left) * (nums[right] - nums[right - 1])
            while sums > k and left <= right:
                sums -= nums[right] - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.maxFrequency([1, 4, 8, 13], 5))
