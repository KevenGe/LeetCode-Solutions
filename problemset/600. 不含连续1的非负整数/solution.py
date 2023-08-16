# 600. 不含连续1的非负整数
# https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/

################################################################################


class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 34
        dp[0] = 1
        dp[1] = 1
        for i in range(2, 34):
            dp[i] = dp[i - 1] + dp[i - 2]

        res = 0
        pre = 0
        t = 1 << 31
        for i in range(32):
            if t & n:
                res += dp[32 - i]

                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0

            t = t >> 1
            if i == 31:
                res += 1

        return res


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.findIntegers(5))

