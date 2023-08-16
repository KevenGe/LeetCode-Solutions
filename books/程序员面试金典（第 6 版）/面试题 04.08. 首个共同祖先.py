# 面试题 04.08. 首个共同祖先
# https://leetcode-cn.com/problems/first-common-ancestor-lcci/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (root is None):
            return None

        if root.val == p.val:
            return p
        if root.val == q.val:
            return q

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l is None:
            if r is None:
                return None
            else:
                return r
        else:
            if r is None:
                return l
            else:
                return root
