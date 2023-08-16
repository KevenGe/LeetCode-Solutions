# 1706. 球会落何处
# https://leetcode-cn.com/problems/where-will-the-ball-fall/


from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = list(range(len(grid[0])))
        for line in grid:
            for j,i in enumerate(ans):
                if i == -1:
                    continue
                l = line[i]

                if l == 1 and i + 1 < len(grid[0]) and line[i + 1] == 1:
                    ans[j] += 1
                elif l == -1 and i - 1 >= 0 and line[i - 1] == -1:
                    ans[j] -= 1
                else:
                    ans[j] = -1
        return ans


if __name__ == "__main__":
    pass
