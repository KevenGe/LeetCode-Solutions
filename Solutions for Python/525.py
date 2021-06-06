from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        sum = 0
        bef = {0: -1}
        ans = 0
        for index, num in enumerate(nums):
            sum += 1 if num == 1 else -1
            if sum in bef:
                ans = max(ans, index - bef.get(sum))
            else:
                bef[sum] = index
        return ans
