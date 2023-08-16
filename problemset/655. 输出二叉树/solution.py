# 655. 输出二叉树
# https://leetcode.cn/problems/print-binary-tree/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            return 1 + max(get_height(root.left), get_height(root.right))

        height = get_height(root) - 1
        m = height + 1
        n = 2 ** (height + 1) - 1
        ans = [["" for _ in range(n)] for _ in range(m)]

        def fill(root: Optional[TreeNode], r: int, c: int, ans: List[List[str]]):
            if root:
                ans[r][c] = str(root.val)
                fill(root.left, r + 1, c - 2 ** (height - r - 1), ans)
                fill(root.right, r + 1, c + 2 ** (height - r - 1), ans)

        fill(root, 0, (n - 1) // 2, ans)
        return ans

