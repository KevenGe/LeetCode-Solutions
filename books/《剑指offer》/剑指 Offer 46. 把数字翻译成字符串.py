# 剑指 Offer 46. 把数字翻译成字符串
# https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/


class Solution:
    def translateNum(self, num: int) -> int:
        strs = list(str(num))
        if len(strs) == 1:
            return 1
        else:
            dp = [0] * len(strs)
            dp[0] = 1
            if strs[0] == "1" or (strs[0] == "2" and strs[1] < "6" and strs[1] >= "0"):
                dp[1] = 2
            else:
                dp[1] = 1

            for i in range(2, len(strs)):
                if strs[i - 1] == "0":
                    dp[i] = dp[i - 1]
                elif strs[i - 1] == "1":
                    dp[i] = dp[i - 1] + dp[i - 2]
                elif strs[i - 1] == "2":
                    if strs[i] < "6" and strs[i] >= "0":
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1]
            return dp[len(strs) - 1]


if __name__ == "__main__":
    solution = Solution()
