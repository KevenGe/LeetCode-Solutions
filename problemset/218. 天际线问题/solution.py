# 218. 天际线问题
# https://leetcode-cn.com/problems/the-skyline-problem/


################################################################################
from typing import List
import heapq
from functools import cmp_to_key


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        que = []
        for building in buildings:
            que.append([building[0], building[2], True])
            que.append([building[1], building[2], False])

        def sortCmp(a, b):
            if a[0] != b[0]:
                return a[0] - b[0]
            else:
                if a[1] != b[1]:
                    return b[1] - a[1]
                else:
                    if a[2]:
                        return -1
                    if b[2]:
                        return 1
                    return 0

        que.sort(key=cmp_to_key(sortCmp))

        # print(que)

        hei = [0]
        heapq.heapify(hei)

        ans = []

        waitToDelete = {}

        for s, h, up in que:
            if up:
                if h > -hei[0]:
                    if len(ans) != 0 and ans[-1][0] == s:
                        ans[-1][1] = h
                    else:
                        ans.append([s, h])
                heapq.heappush(hei, -h)
            else:
                if h == -hei[0]:
                    heapq.heappop(hei)
                    while True:
                        if -hei[0] in waitToDelete and waitToDelete[-hei[0]] > 0:
                            waitToDelete[-hei[0]] -= 1
                            heapq.heappop(hei)
                        else:
                            break

                    if -hei[0] != h:
                        if len(ans) != 0 and ans[-1][0] == s:
                            ans[-1][1] = -hei[0]
                        else:
                            ans.append([s, -hei[0]])
                elif h < -hei[0]:
                    if h in waitToDelete:
                        waitToDelete[h] += 1
                    else:
                        waitToDelete[h] = 1
        return ans


################################################################################


if __name__ == "__main__":
    so = Solution()
    # print(
    #     so.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
    # )
    print(so.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]))
    # print(so.getSkyline([[0, 2, 3], [2, 5, 3]]))
    # print(so.getSkyline([[2, 9, 10], [9, 12, 15]]))
