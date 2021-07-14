# 1818. 绝对差值和
#

from typing import List
import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        nums1s = sorted(nums1)

        maxn = 0
        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            ans += diff

            j = bisect.bisect_left(nums1s, nums2[i])
            if j < len(nums1s):
                maxn = max(maxn, diff - abs(nums1s[j] - nums2[i]))

            if j - 1 >= 0:
                maxn = max(maxn, diff - abs(nums1s[j - 1] - nums2[i]))

        return (ans - maxn + 1000000007) % 1000000007


if __name__ == "__main__":
    so = Solution()
    print(so.minAbsoluteSumDiff([2, 4, 6, 8, 10], [2, 4, 6, 8, 10]))

