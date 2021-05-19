from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dict1 = set(nums)
        res = 1
        for num in nums:
            if num-1 in dict1:
                continue
            if num+1 in dict1:
                ans = 2
                t = num + 1
                while t + 1 in dict1:
                    ans += 1
                    t += 1
                res = max(res, ans)
        return res
