# 797. 所有可能的路径
# https://leetcode-cn.com/problems/all-paths-from-source-to-target/
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        self.visited = [False] * len(graph)
        self.visited[0] = True
        self.tmpPath = [0]
        def dfs(i):
            if i == len(graph)-1:
                self.ans.append(self.tmpPath.copy())
                return
            for target in graph[i]:
                if self.visited[target] == False:
                    self.visited[target] = True
                    self.tmpPath.append(target)
                    dfs(target)
                    self.tmpPath.pop()
                    self.visited[target] = False
        dfs(0)
        return self.ans


if __name__ == "__main__":
    solution = Solution()
