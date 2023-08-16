# LCP 33. 蓄水
# https://leetcode-cn.com/problems/o8SXZn/

################################################################################
from typing import List
from functools import reduce
import math


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:

        ans = 100000

        maxn = 0
        for i in range(len(bucket)):
            if vat[i] == 0:
                continue
            if bucket[i] == 0:
                maxn = max(maxn, vat[i])
                continue
            maxn = max(maxn, math.ceil(vat[i] / bucket[i]))

        for i in range(1, maxn + 1):
            t = 0
            for j in range(len(bucket)):
                if vat[j] == 0:
                    continue

                m = math.ceil(vat[j] / i) - bucket[j]
                t += m if m > 0 else 0

            ans = min(ans, t + i)

        return ans if ans != 100000 else 0


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.storeWater([1, 3], [6, 6]))

