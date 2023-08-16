# 1743. 从相邻元素对还原数组
# https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/

from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        s = set()
        for adjacentPair in adjacentPairs:
            for a in adjacentPair:
                if s.__contains__(a):
                    s.remove(a)
                else:
                    s.add(a)

        d = dict()
        for adjacentPair in adjacentPairs:
            if d.__contains__(adjacentPair[0]):
                d[adjacentPair[0]].append(adjacentPair[1])
            else:
                d[adjacentPair[0]] = [adjacentPair[1]]

            if d.__contains__(adjacentPair[1]):
                d[adjacentPair[1]].append(adjacentPair[0])
            else:
                d[adjacentPair[1]] = [adjacentPair[0]]

        start = s.pop()
        ans = [start]
        beforeStart = start
        while True:
            tar = None
            for i in d[start]:
                if i != beforeStart:
                    tar = i
                    break
            if tar is None:
                break
            ans.append(tar)
            beforeStart = start
            start = tar
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.restoreArray([[2, 1], [3, 4], [3, 2]]))
