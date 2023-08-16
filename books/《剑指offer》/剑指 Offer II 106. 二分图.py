# 剑指 Offer II 106. 二分图
# https://leetcode.cn/problems/vEAB3K/

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color_list = [0] * len(graph)

        def dfs(color_list: List[int], node_idx: int):
            for neighbor_idx in graph[node_idx]:
                if color_list[neighbor_idx] == 0:
                    color_list[neighbor_idx] = - color_list[node_idx]
                    if not dfs(color_list, neighbor_idx):
                        return False
                elif color_list[neighbor_idx] == 1 or color_list[neighbor_idx] == -1:
                    if color_list[neighbor_idx] != -color_list[node_idx]:
                        return False
            return True

        for node_idx in range(len(graph)):
            if color_list[node_idx] == 0:
                color_list[node_idx] = 1
                if not dfs(color_list, node_idx):
                    return False

        return True


if __name__ == "__main__":
    so = Solution()
    assert so.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) == False
    assert so.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) == True
