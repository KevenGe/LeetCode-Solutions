# 1038. 把二叉搜索树转换为累加树
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        self.t = 0

        def rrr(root: TreeNode):
            if root:
                rrr(root.right)

                root.val += self.t
                self.t = root.val

                rrr(root.left)

        rrr(root)
        return root
