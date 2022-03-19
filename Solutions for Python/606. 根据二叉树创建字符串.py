# 606. 根据二叉树创建字符串
# https://leetcode-cn.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        else:
            ans = str(root.val)

            if root.left is None:
                if root.right is None:
                    pass
                else:
                    ans += "()({})".format(self.tree2str(root.right))
            else:
                if root.right is None:
                    ans += "({})".format(self.tree2str(root.left))
                else:
                    ans += "({0})({1})".format(self.tree2str(root.left), self.tree2str(root.right))
            
            return ans
