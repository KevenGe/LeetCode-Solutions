# 1189. “气球” 的最大数量
# https://leetcode-cn.com/problems/maximum-number-of-balloons/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {
            "b":0,
            "a":0,
            "l":0,
            "o":0,
            "n":0
        }
        for ch in text:
            if ch in d:
                d[ch] += 1

        ans = 100000
        for ch,i in [("b", 1), ("a", 1), ("l", 2), ("o", 2), ("n", 1)]:
            ans = min(ans, d[ch] // i)
        return ans
