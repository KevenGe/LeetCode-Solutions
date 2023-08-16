# 658. 找到 K 个最接近的元素
# https://leetcode.cn/problems/find-k-closest-elements/

from typing import List
from functools import cmp_to_key

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def cmp(a:int,b:int):
            if abs(a-x) == abs(b-x):
                return a - b
            else:
                return abs(a-x) - abs(b-x)
        arr.sort(key=cmp_to_key(cmp))
        return sorted(arr[:k])
