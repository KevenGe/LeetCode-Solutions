# 675. 为高尔夫比赛砍树
# https://leetcode.cn/problems/cut-off-trees-for-golf-event/


from typing import List, Tuple
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        allTreeHeights = [(1, 0, 0)]  # heihgt, i, j

        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    allTreeHeights.append((forest[i][j], i, j))

        allTreeHeights.sort(key=lambda x: x[0])

        def computeMinDistance(s: Tuple[int, int, int], t: Tuple[int, int, int]) -> int:
            if s[1] == t[1] and s[2] == t[2]:
                return 0

            visited = [[False for j in range(len(forest[0]))]
                       for i in range(len(forest))]
            # print(s[1])
            # print(s[2])
            visited[s[1]][s[2]] = True

            q = deque()
            q.append((s[1], s[2]))
            levelNum = 1
            nextLevelNum = 0
            dis = 1
            while levelNum != 0:
                levelNum -= 1
                ni, nj = q.popleft()

                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ti = ni + di
                    tj = nj + dj

                    if 0 <= ti < len(forest) and 0 <= tj < len(forest[0]):
                        if ti == t[1] and tj == t[2]:
                            return dis

                        if forest[ti][tj] > 0 and visited[ti][tj] == False:
                            q.append((ti, tj))
                            visited[ti][tj] = True
                            nextLevelNum += 1

                if levelNum == 0:
                    levelNum = nextLevelNum
                    nextLevelNum = 0
                    dis += 1

            return -1

        ans = 0
        for i in range(len(allTreeHeights)-1):
            s = allTreeHeights[i]
            t = allTreeHeights[i + 1]
            r = computeMinDistance(s, t)
            if r == -1:
                return -1
            else:
                ans += r
        return ans


if __name__ == "__main__":
    so = Solution()
    # print(so.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))
    # print(so.cutOffTree([[1,2,3],[0,0,0],[7,6,5]]))
    print(so.cutOffTree([[2,3,4],[0,0,5],[8,7,6]]))
