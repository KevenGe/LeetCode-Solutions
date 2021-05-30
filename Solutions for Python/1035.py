from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == 0 or len(nums2) == 0:
            return 0

        dp = [ [0 for _ in  range((len(nums2) + 1))] for j in range(len(nums1)+1)]

        dict1 = dict()

        dict2 = dict([(nums2[i - 1], i) for i in range(1, len(nums2) + 1)])

        for i in range(1, len(nums1) + 1):
            dict1[nums1[i - 1]] = i

            for j in range(1, len(nums2) + 1):
                if nums2[j - 1] in dict1:
                    dp[i][j] = max(dp[i][j - 1], dp[dict1[nums2[j - 1]] - 1][j - 1] + 1)
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[len(nums1)][len(nums2)]


if __name__ == "__main__":
    so = Solution()
    print(so.maxUncrossedLines([1, 4, 2], [1, 2, 4]))

