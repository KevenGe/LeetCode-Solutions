# 剑指 Offer II 005. 单词长度的最大乘积
# https://leetcode.cn/problems/aseY1I/

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        nws = [set(w) for w in words]

        ans = 0
        for i, nw1 in enumerate(nws):
            for j, nw2 in enumerate(nws):
                if nw1 != nw2 and len(nw1.intersection(nw2)) == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
