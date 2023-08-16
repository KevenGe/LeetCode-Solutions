# 671. 二叉树中第二小的节点
# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None or root.left is None or root.right is None:
            return -1

        l2 = root.left.val
        if root.val == root.left.val:
            l2 = self.findSecondMinimumValue(root.left)

        r2 = root.right.val
        if root.val == root.right.val:
            r2 = self.findSecondMinimumValue(root.right)

        if l2 == -1:
            if r2 == -1:
                return -1
            else:
                return r2
        else:
            if r2 == -1:
                return l2
            else:
                return min(l2, r2)


if __name__ == "__main__":
    solution = Solution()
