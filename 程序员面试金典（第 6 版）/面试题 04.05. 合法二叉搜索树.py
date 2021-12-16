# 面试题 04.05. 合法二叉搜索树
# https://leetcode-cn.com/problems/legal-binary-search-tree-lcci/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(root, l_limit, r_limit):
            if root is None or l_limit >= r_limit:
                return True

            if l_limit < root.val < r_limit:
                return helper(root.left, l_limit, root.val) and helper(root.right, root.val, r_limit)
            return False

        return helper(root, -float('inf'), float('inf'))
