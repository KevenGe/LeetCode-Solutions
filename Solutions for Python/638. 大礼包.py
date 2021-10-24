# 638. 大礼包
# https://leetcode-cn.com/problems/shopping-offers/

################################################################################
from typing import List
import copy


class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        def runs(index: int, dp):
            if index < len(needs):
                t = runs(index + 1, dp)
                t2 = [copy.copy(t) for j in range(needs[index])]
                return t2
            else:
                return 0

        dp = runs(999999999, [])
        print(dp)

        def runs(index: int, index2: List[int], dp):
            if index < len(needs) - 1:
                for i in range(needs[index]):
                    index2[index] = i
                    runs(index + 1, index2, dp)
            else:
                for j in range(needs[index]):
                    if j == 0:
                        pass


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]))
