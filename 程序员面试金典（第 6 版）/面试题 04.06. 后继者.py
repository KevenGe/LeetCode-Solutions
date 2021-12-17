# 面试题 04.06. 后继者
# https://leetcode-cn.com/problems/successor-lcci/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:


        self.state = 0
        self.ans = None

        def dfs(root):
            if root is None or self.state == 2:
                return

            dfs(root.left)
            if self.state == 0:
                if root.val == p.val:
                    self.state = 1
            elif self.state == 1:
                self.ans = root
                self.state = 2
            dfs(root.right)

        dfs(root)
        return self.ans
