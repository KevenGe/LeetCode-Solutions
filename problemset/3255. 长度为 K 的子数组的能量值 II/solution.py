from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        ans = []
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur_len += 1
            else:
                cur_len = 1

            if i >= k - 1:
                if cur_len >= k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)

        return ans
