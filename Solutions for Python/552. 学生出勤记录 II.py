# 552. 学生出勤记录 II
# https://leetcode-cn.com/problems/student-attendance-record-ii/


class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[0 for k in range(3)] for j in range(2)] for i in range(n + 1)]
        dp[0][0][0] = 1

        m = 10 ** 9 + 7

        for i in range(1, n + 1):

            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % m

            for k in range(3):
                dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % m

            for j in range(2):
                for k in range(2):
                    dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][j][k]) % m

        ans = 0
        for j in range(2):
            for k in range(3):
                ans = (ans + dp[n][j][k]) % m
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkRecord(10101))
