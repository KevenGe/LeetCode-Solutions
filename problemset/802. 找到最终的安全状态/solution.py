# 802. 找到最终的安全状态
# https://leetcode-cn.com/problems/find-eventual-safe-states/

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        status = [0] * len(graph)  # 0:init, 1:is safe, 2 is unsafe, -1:is visiting

        def dfs(i: int, status: List[int]) -> int:
            if status[i] == 0:
                if len(graph[i]) == 0:
                    status[i] = 1
                    return 1

                status[i] = -1
                curStatu = 1
                for t in graph[i]:
                    z = dfs(t, status)
                    if z == 2:
                        curStatu = 2
                        break  # TODO
                status[i] = curStatu
                return curStatu
            elif status[i] == -1:
                status[i] = 2
                return 2
            else:
                return status[i]

        for i in range(len(status)):
            if status[i] == 0:
                dfs(i, status)

        ans = []
        for i in range(len(status)):
            if status[i] == 1:
                ans.append(i)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))