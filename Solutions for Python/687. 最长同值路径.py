# 687. 最长同值路径
# https://leetcode.cn/problems/longest-univalue-path/


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if root:
                left = dfs(root.left)
                right = dfs(root.right)

                left_same = 0
                if root.left is not None and root.val == root.left.val:
                    left_same = left + 1

                right_same = 0
                if root.right is not None and root.val == root.right.val:
                    right_same = right + 1

                ans = max(left_same, right_same)
                self.ans = max(self.ans, left_same + right_same, ans)
                return ans
            else:
                return 0

        dfs(root)
        return self.ans
