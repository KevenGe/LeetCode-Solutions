# 623. 在二叉树中增加一行
# https://leetcode.cn/problems/add-one-row-to-tree/

from typing import Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def more(root: Optional[TreeNode], val: int, depth: int, is_Left: bool) -> Optional[TreeNode]:
            if depth == 1:
                if is_Left:
                    root = TreeNode(val, left=root, right=None)
                else:
                    root = TreeNode(val, left=None, right=root)
                return root

            if root is None:
                return root

            root.left = more(root.left, val, depth - 1, True)
            root.right = more(root.right, val, depth - 1, False)
            return root

        return more(root, val, depth, True)


if __name__ == "__main__":
    so = Solution()
