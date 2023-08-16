# 1200. 最小绝对差
# https://leetcode.cn/problems/minimum-absolute-difference/

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()

        sub_dis = float('inf')
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) < sub_dis:
                sub_dis = abs(arr[i + 1] - arr[i])

        ans = []
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) == sub_dis:
                ans.append([arr[i], arr[i + 1]])

        return ans
