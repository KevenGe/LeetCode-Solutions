# 391. 完美矩形
# https://leetcode-cn.com/problems/perfect-rectangle/

################################################################################
from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        tris = {}

        def add(x, y, tris):
            if x in tris:
                if y in tris[x]:
                    tris[x][y] += 1
                else:
                    tris[x][y] = 1
            else:
                tris[x] = {y: 1}

        area = 0
        minx = 10000000000
        miny = 10000000000
        maxa = -10000000000
        maxb = -10000000000

        for x, y, a, b in rectangles:
            add(x, y, tris)
            add(a, y, tris)
            add(a, b, tris)
            add(x, b, tris)

            area += (b - y) * (a - x)
            minx = min(minx, x)
            miny = min(miny, y)
            maxa = max(maxa, a)
            maxb = max(maxb, b)

        if (
            area != (maxa - minx) * (maxb - miny)
            or (miny in tris[minx] and tris[minx][miny] != 1)
            or (maxb in tris[minx] and tris[minx][maxb] != 1)
            or (miny in tris[maxa] and tris[maxa][miny] != 1)
            or (maxb in tris[maxa] and tris[maxa][maxb] != 1)
        ):
            return False

        cou = 0
        for k, v in tris.items():
            for k2, v2 in v.items():
                if v2 == 2 or v2 == 4:
                    pass
                elif v2 == 1:
                    cou += 1
                else:
                    return False

        return cou == 4


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.isRectangleCover([[1,1,2,2],[0,1,1,2],[1,0,2,1],[0,2,3,3],[2,0,3,3]]))
