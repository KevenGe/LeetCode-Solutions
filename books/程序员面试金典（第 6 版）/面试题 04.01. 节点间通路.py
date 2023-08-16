# 面试题 04.01. 节点间通路
# https://leetcode-cn.com/problems/route-between-nodes-lcci/

from typing import List, Dict


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        graph_dict:Dict[int,List[int]] = dict()
        for i in range(n):
            graph_dict[i] = []
        for s,t in graph:
            graph_dict[s].append(t)

        have_dict = [False for i in range(n)]

        def dfs(have_dict, start):

            if have_dict[start] == True or have_dict[target] == True:
                return

            if start == target:
                have_dict[target] = True
                return

            have_dict[start] = True

            for t in graph_dict[start]:
                if have_dict[t] == False:
                    dfs(have_dict, t)

        dfs(have_dict, start)
        return have_dict[target]
