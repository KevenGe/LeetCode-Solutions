# 930. 和相同的二元子数组
# https://leetcode-cn.com/problems/binary-subarrays-with-sum/

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = {0: 1}
        sum = 0
        ans = 0
        for num in nums:
            sum += num

            if sum - goal in cnt:
                ans += cnt[sum - goal]

            if sum in cnt:
                cnt[sum] += 1
            else:
                cnt[sum] = 1

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
