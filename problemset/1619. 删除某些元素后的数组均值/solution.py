# 1619. 删除某些元素后的数组均值
# https://leetcode.cn/problems/mean-of-array-after-removing-some-elements/


from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        k = int(len(arr) * 0.05)
        narr = arr[k:-k]
        ans = sum(narr) / len(narr)
        return ans
