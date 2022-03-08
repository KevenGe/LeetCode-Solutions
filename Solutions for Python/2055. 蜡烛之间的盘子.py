# 2055. 蜡烛之间的盘子
# https://leetcode-cn.com/problems/plates-between-candles/

from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        right_close_candles = [-1]*len(s)
        latest_right_close_candle = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == "|":
                right_close_candles[i] = i
                latest_right_close_candle = i
            else:
                right_close_candles[i] = latest_right_close_candle

        left_close_candles = [-1]*len(s)
        latest_left_close_candle = -1
        for i in range(len(s)):
            if s[i] == "|":
                left_close_candles[i] = i
                latest_left_close_candle = i
            else:
                left_close_candles[i] = latest_left_close_candle

        plates_sums = [0]*(len(s)+2)
        for i in range(len(s)):
            if s[i] == "|":
                plates_sums[i+1] = plates_sums[i]
            else:
                plates_sums[i+1] = plates_sums[i] + 1

        # print(right_close_candles)
        # print(left_close_candles)
        # print(plates_sums)

        ans = []
        for l,r in queries:
            l = right_close_candles[l]
            r = left_close_candles[r]

            if l == -1 or r == -1 or l >= r:
                ans.append(0)
                continue

            ans.append(plates_sums[r+1] - plates_sums[l])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.platesBetweenCandles(
        "**|**|***|",
        [[2, 5], [5, 9]]
    ))
