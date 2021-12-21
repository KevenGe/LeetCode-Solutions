# 面试题 04.12. 求和路径
# https://leetcode-cn.com/problems/paths-with-sum-lcci/

from typing import Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans_count = 0

        def dfs(dfs_root: TreeNode, node_sum: Dict[int, int]):
            if dfs_root is None:
                return

            new_node_sum = dict([(k + dfs_root.val, v) for k, v in node_sum.items()])
            if dfs_root.val in new_node_sum:
                new_node_sum[dfs_root.val] += 1
            else:
                new_node_sum[dfs_root.val] = 1

            if sum in new_node_sum:
                self.ans_count += new_node_sum[sum]

            dfs(dfs_root.left, new_node_sum.copy())
            dfs(dfs_root.right, new_node_sum.copy())

        dfs(root, {})

        return self.ans_count
