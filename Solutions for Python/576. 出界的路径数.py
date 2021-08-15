# 576. 出界的路径数
# https://leetcode-cn.com/problems/out-of-boundary-paths/


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:

        dp = [[0 for j in range(n)] for i in range(m)]
        dp[startRow][startColumn] = 1

        bigMod = 10 ** 9 + 7

        count = 0

        for i in range(maxMove):
            newDp = [[0 for j in range(n)] for i in range(m)]
            for j in range(m):
                for z in range(n):
                    if dp[j][z] >= 1:
                        for x, y in [(j - 1, z), (j + 1, z), (j, z - 1), (j, z + 1)]:
                            if x < 0 or x >= m or y < 0 or y >= n:
                                count = (dp[j][z] + count) % bigMod
                            else:
                                newDp[x][y] = (dp[j][z] + newDp[x][y]) % bigMod
            dp = newDp
        return count


if __name__ == "__main__":
    solution = Solution()
