# 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root.val == p.val or root.val == q.val:
            return root

        if p.val < root.val:
            if q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return root
        else:
            if q.val < root.val:
                return root
            else:
                return self.lowestCommonAncestor(root.right, p, q)


if __name__ == "__main__":
    solution = Solution()
