# 599. 两个列表的最小索引总和
# https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = dict([[v,i] for i,v in enumerate(list1)])


        ans = []
        minSum = float('inf')
        for i,v in enumerate(list2):
            if v in d1:
                if d1[v] + i < minSum:
                    minSum = d1[v] + i
                    ans = [v]
                elif d1[v] + i == minSum:
                    ans.append(v)
        
        return ans
