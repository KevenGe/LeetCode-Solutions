# 1588. 所有奇数长度子数组的和
# https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            n = ((i - 0) // 2 + 1) * ((len(arr) - 1 - i) // 2 + 1) + (
                (i - 0 + 1) // 2
            ) * ((len(arr) - i) // 2)

            ans += arr[i] * n
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
