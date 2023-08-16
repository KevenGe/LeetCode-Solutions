# 563. 二叉树的坡度
# https://leetcode-cn.com/problems/binary-tree-tilt/

################################################################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:

        self.ans = 0

        def dfs(root: TreeNode):
            if root is None:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            self.ans += abs(r - l)
            return l + r + root.val

        dfs(root)
        return self.ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
