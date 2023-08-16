# 786. 第 K 个最小的素数分数
# https://leetcode-cn.com/problems/k-th-smallest-prime-fraction/


################################################################################


from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l = 0
        r = 1

        while True:
            m = (l + r) / 2
            cou = 0

            x = 0
            y = 1

            for i in range(1, len(arr)):
                for j in range(i):
                    if arr[j] / arr[i] <= m:
                        cou += 1
                        if arr[j] * y > arr[i] * x:
                            x = arr[j]
                            y = arr[i]
                    else:
                        break

            if cou == k:
                return [x, y]
            elif cou > k:
                r = m
            else:
                l = m

################################################################################
