# 218. 天际线问题
# https://leetcode-cn.com/problems/the-skyline-problem/

from typing import List
import heapq


class Node:
    def __init__(self, x, h, l):
        self.x = x
        self.h = h
        self.l = l

    def __lt__(self, other):
        if self.x == other.x:
            return self.h < other.h
        return self.x < other.x


class PriItem:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x > other.x

    def __eq__(self, other):
        return self.x == other.x


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        d = []
        for building in buildings:
            d.append(Node(building[0], building[2], True))
            d.append(Node(building[1], building[2], False))
        d.sort()

        ans = []
        pri = [PriItem(0)]
        lastHeight = 0

        for node in d:
            if node.l:
                heapq.heapify(pri)
                height = pri[0].x

                if node.h > height:
                    if len(ans) != 0 and node.x == ans[len(ans) - 1][0]:
                        if node.h == lastHeight:
                            del ans[len(ans) - 1]
                        else:
                            del ans[len(ans) - 1]
                            ans.append([node.x, node.h])
                    else:
                        ans.append([node.x, node.h])

                pri.append(PriItem(node.h))
            else:
                i = pri.index(PriItem(node.h))
                del pri[i]
                heapq.heapify(pri)

                height = pri[0].x

                if height < node.h:
                    lastHeight = node.h
                    ans.append([node.x, height])

        return ans


if __name__ == "__main__":
    so = Solution()
    print(
        so.getSkyline([[4, 9, 10], [4, 9, 15], [4, 9, 12], [10, 12, 10], [10, 12, 8]])
    )

