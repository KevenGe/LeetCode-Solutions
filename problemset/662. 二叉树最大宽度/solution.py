# 662. 二叉树最大宽度
# https://leetcode.cn/problems/maximum-width-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        depth_left = dict()
        depth_right = dict()

        def dfs(root: Optional[TreeNode], depth: int, id: int):
            if root:
                if depth not in depth_left:
                    depth_left[depth] = id
                else:
                    depth_left[depth] = min(depth_left[depth], id)

                if depth not in depth_right:
                    depth_right[depth] = id
                else:
                    depth_right[depth] = max(depth_right[depth], id)

                dfs(root.left, depth + 1, 2 * id + 1)
                dfs(root.right, depth + 1, 2 * id + 2)

        dfs(root, 0, 0)

        ans = 1
        for k, v in depth_left.items():
            ans = max(ans, depth_right[k] - depth_left[k] + 1)

        return ans

