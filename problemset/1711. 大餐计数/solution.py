# 1711. 大餐计数
# https://leetcode-cn.com/problems/count-good-meals/

from typing import List
from collections import Counter


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:

        targets = set()
        t = 1
        for i in range(32):
            targets.add(t)
            t = t << 1

        ans = 0

        counts = Counter(deliciousness)
        for c in counts:
            if c * 2 in targets:
                if counts[c] > 1:
                    ans = (ans +  (counts[c] * (counts[c] - 1)) // 2) % 1000000007
            
            for t in targets:
                if (t := t - c) in counts and c < t:
                    ans = (ans +  counts[c] * counts[t]) % 1000000007

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.countPairs([1, 3, 5, 7, 9]))

