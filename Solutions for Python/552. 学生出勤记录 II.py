# 552. 学生出勤记录 II
# https://leetcode-cn.com/problems/student-attendance-record-ii/


class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[0 for k in range(3)] for j in range(2)]
        dp[0][0] = 1

        m = 10 ** 9 + 7

        for i in range(1, n + 1):
            dpNew = [[0 for k in range(3)] for j in range(2)]

            for j in range(2):
                for k in range(3):
                    dpNew[j][0] = (dpNew[j][0] + dp[j][k]) % m

            for k in range(3):
                dpNew[1][0] = (dpNew[1][0] + dp[0][k]) % m

            for j in range(2):
                for k in range(2):
                    dpNew[j][k + 1] = (dpNew[j][k + 1] + dp[j][k]) % m
            
            dp = dpNew

        ans = 0
        for j in range(2):
            for k in range(3):
                ans = (ans + dp[j][k]) % m
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkRecord(10101))
