# 5965. 相同元素的间隔之和
# https://leetcode-cn.com/problems/intervals-between-identical-elements/

from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        te_dcit = {}
        for i,a in enumerate(arr):
            if a in te_dcit:
                te_dcit[a].append(i)
            else:
                te_dcit[a] = [i]

        ans = [0] * len(arr)

        for k,v in te_dcit.items():
            start = 0
            for i in range(1, len(v)):
                start += v[i] - v[0]
            ans[v[0]] = start
            for i in range(1, len(v)):
                start = start - (v[i] - v[i-1]) * (len(v) - i - 1) + (v[i] - v[i-1]) * (i - 1)
                ans[v[i]] = start
        return ans