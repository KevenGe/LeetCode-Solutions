from typing import List


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        edge_map: dict[int, list[int]] = dict()
        for a, b in edges:
            if a not in edge_map:
                edge_map[a] = []
            edge_map[a].append(b)
            if b not in edge_map:
                edge_map[b] = []
            edge_map[b].append(a)

        visited = [False] * n
        self.ans = 0

        def dfs(node: int) -> int:
            visited[node] = True

            child_node_nums = []
            for child_node in edge_map[node]:
                if visited[child_node]:
                    continue
                child_node_nums.append(dfs(child_node))

            if len(child_node_nums) == 0 or len(set(child_node_nums)) == 1:
                self.ans += 1

            return sum(child_node_nums) + 1

        dfs(0)
        return self.ans
