# 2059. 转化数字的最小运算数
# https://leetcode-cn.com/problems/minimum-operations-to-convert-number/

################################################################################
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        
        x = start
        waitToCalculate = [x]
        calculateTimes = 1
        visited = set()
        while len(waitToCalculate)!=0:
            nextWaitToCalculate = set()
            for xx in waitToCalculate:
                if xx in visited:
                    continue
                visited.add(xx)
                for num in nums:
                    t = [xx + num, xx - num , xx ^ num]
                    for tmp in t:
                        if tmp == goal:
                            return calculateTimes
                        if 0 <= tmp <= 1000:
                            nextWaitToCalculate.add(tmp)
            waitToCalculate = nextWaitToCalculate
            calculateTimes += 1
        return -1

################################################################################

if __name__ == "__main__":
    solution = Solution()
