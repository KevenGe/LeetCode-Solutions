from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        dp = [0 for i in range(len(arr) + 1)]
        for i in range(1, len(arr) + 1):
            dp[i] = dp[i - 1] ^ arr[i - 1]

        ans = [0 for i in range(len(queries))]
        for i in range(len(queries)):
            l, r = queries[i]
            ans[i] = dp[r + 1] ^ dp[l]
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))

