# 1518. 换酒问题
# https://leetcode-cn.com/problems/water-bottles/


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        ans = numBottles
        while numBottles >= numExchange:
            last = numBottles % numExchange
            newOne = numBottles // numExchange
            ans += newOne
            numBottles = last + newOne
        return ans
