# 剑指 Offer 27. 二叉树的镜像
# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        t = self.mirrorTree(root.left)
        root.left = self.mirrorTree(root.right)
        root.right = t
        return root


if __name__ == "__main__":
    solution = Solution()
