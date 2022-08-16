# 1417. 重新格式化字符串
# https://leetcode.cn/problems/reformat-the-string/

import string
from typing import List


class Solution:
    def reformat(self, s: str) -> str:
        alphas = []
        nums = []

        for st in s:
            if st in string.digits:
                nums.append(st)
            else:
                alphas.append(st)

        if abs(len(alphas) - len(nums)) > 1:
            return ""

        def concat(a: List[str], b: List[str]) -> str:
            if len(a) < len(b):
                return concat(b, a)

            ans = []

            for i in range(min(len(a), len(b))):
                ans.append(a[i])
                ans.append(b[i])

            if len(a) > len(b):
                ans.append(a[-1])

            return "".join(ans)

        return concat(alphas, nums)
