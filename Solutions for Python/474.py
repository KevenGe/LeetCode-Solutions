from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        def g(s: str):
            m2 = 0
            n2 = 0
            for ss in s:
                if ss == "0":
                    m2 += 1
                else:
                    n2 += 1
            return m2, n2

        for st in strs:
            m2, n2 = g(st)
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= m2 and j >= n2:
                        dp[i][j] = max(dp[i][j], dp[i - m2][j - n2] + 1)

        return dp[m][n]


if __name__ == "__main__":
    so = Solution()
    print(so.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))

