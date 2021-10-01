# 1436. 旅行终点站
# https://leetcode-cn.com/problems/destination-city/

################################################################################
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict(paths)

        def getTarget(city):
            if city not in d:
                return city
            else:
                return getTarget(d[city])

        for s, t in paths:
            t2 = getTarget(t)
            if t2 is not None:
                return t2


################################################################################


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.destCity(
            [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
        )
    )

