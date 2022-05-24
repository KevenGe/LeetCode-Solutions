# 965. 单值二叉树
# https://leetcode.cn/problems/univalued-binary-tree/

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        def isIt(root:TreeNode, val:int) -> bool:
            if root is None:
                return True
            else:
                if root.val == val:
                    return isIt(root.left, val) and isIt(root.right, val)
                else:
                    return False
        
        return isIt(root, root.val)

