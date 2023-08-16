# 面试题 17.10. 主要元素
# https://leetcode-cn.com/problems/find-majority-element-lcci/

# Boyer-Moore 投票算法

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                if num == candidate:
                    count += 1
                else:
                    count -= 1

        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate
        else:
            return -1


if __name__ == "__main__":
    so = Solution()

