# 2049. 统计最高分的节点数目
# https://leetcode-cn.com/problems/count-nodes-with-the-highest-score/


from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        children = [[] for i in range(len(parents))]
        for i, parent in enumerate(parents):
            if parent != -1:
                children[parent].append(i)

        node_nums = [0] * len(parents)

        def sum_num(i, node_nums):
            s = 1
            for chi in children[i]:
                sum_num(chi, node_nums)
                s += node_nums[chi]
            node_nums[i] = s

        sum_num(0, node_nums)

        maxK = -1
        maxN = 0

        # cal
        for i in range(len(parents)):
            s = 1
            if parents[i] != -1:
                s *= (node_nums[0] - node_nums[i])
            for chi in children[i]:
                s *= node_nums[chi]

            if s > maxK:
                maxK = s
                maxN = 1
            elif s == maxK:
                maxN += 1

        return maxN


if __name__ == '__main__':
    solution = Solution()
    print(solution.countHighestScoreNodes([-1,2,0,2,0]))


