# 5964. 执行所有后缀指令
# https://leetcode-cn.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = [0] * len(s)

        def dfs(i, pos):
            if i == n or not (pos[0] >= 0 and pos[0] < n - 1 and pos[1] >= 0 and pos[1] < n - 1):
                pass

        for i in range(len(s)):
            if ans[i] == -1:
                dfs(i, startPos)

        las_pos = [0, 0]
        changes = []
        for i in range(len(s)):
            if s[i] == "L":
                las_pos = [las_pos[0], las_pos[1] - 1]
            elif s[i] == "R":
                las_pos =[las_pos[0], las_pos[1] + 1]
            elif s[i] == "U":
                las_pos =[las_pos[0] - 1, las_pos[1]]
            elif s[i] == "D":
                las_pos =[las_pos[0] + 1, las_pos[1]]
            changes.append(las_pos)

        for i in range(len(s)):
            pos = startPos[:]

            for j in range(i, len(s)):
                pos = [startPos[0] + changes[j][0], startPos[1] + changes[j][1]]
                if i > 0:
                    pos = [pos[0] - changes[i-1][0], pos[1] - changes[i-1][1]]
                if 0 <= pos[0] <= n - 1 and 0 <= pos[1] <= n - 1:
                    ans[i] += 1
                else:
                    break
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.executeInstructions(3, [0,1], "RRDDLU"))
