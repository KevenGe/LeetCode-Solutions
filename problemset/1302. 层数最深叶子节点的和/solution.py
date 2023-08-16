# 1302. 层数最深叶子节点的和
# https://leetcode.cn/problems/deepest-leaves-sum/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        self.deep_depth = 0
        self.deep_val = 0

        def dfs(root: Optional[TreeNode], depth: int):
            if root is None:
                return

            if depth == self.deep_depth:
                self.deep_val += root.val
            elif depth > self.deep_depth:
                self.deep_depth = depth
                self.deep_val = root.val

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)

        return self.deep_val
