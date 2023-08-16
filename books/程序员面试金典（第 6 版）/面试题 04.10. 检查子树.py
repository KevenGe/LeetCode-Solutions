# 面试题 04.10. 检查子树
# https://leetcode-cn.com/problems/check-subtree-lcci/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSame(t1:TreeNode, t2:TreeNode)->bool:
    if t1 is None and t2 is None:
        return True
    if t1 is not None and t2 is not None and t1.val == t2.val:
        return isSame(t1.left, t2.left) and isSame(t1.right, t2.right)
    return False


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        ans = isSame(t1,t2)
        if ans == False and t1 is not None:
            ans = self.checkSubTree(t1.left, t2)
        if ans == False and t1 is not None:
            ans = self.checkSubTree(t1.right, t2)
        return ans
