# 222. 完全二叉树的节点个数
# https://leetcode.cn/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is not None:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
        else:
            return 0


class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        depth = 0
        t = root
        while t is not None:
            t = t.left
            depth += 1

        if depth == 0:
            return 0
        elif depth == 1:
            return 1

        left = 0
        right = 2 ** (depth - 1)
        while left < right:
            mid = (left + right ) // 2

            t = root
            for i in range(depth - 1):
                if mid & (1 << (depth - 2 - i)):
                    t = t.right
                else:
                    t = t.left

            if t is None:
                right = mid
            else:
                left = mid + 1

        ans = 2 ** (depth-1) - 1 + left
        return ans


