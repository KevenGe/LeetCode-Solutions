# 1005. K 次取反后最大化的数组和
# https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/

################################################################################
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        negativeNum = 0
        for num in nums:
            if num < 0:
                negativeNum += 1

        if negativeNum >= k:
            for i in range(k):
                nums[i] = -nums[i]
        else:
            for i in range(negativeNum):
                nums[i] = -nums[i]

            if (k - negativeNum) % 2 == 1:
                nums.sort()
                nums[0] = -nums[0]

        return sum(nums)


################################################################################

if __name__ == '__main__':
    solution = Solution()
    print(solution.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
