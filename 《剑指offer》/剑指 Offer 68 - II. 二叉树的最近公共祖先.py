# 剑指 Offer 68 - II. 二叉树的最近公共祖先
# https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def getLines(root: TreeNode, p: TreeNode):
            if root is None:
                return []

            if root.val == p.val:
                return [root]

            t1 = getLines(root.left, p)
            t2 = getLines(root.right, p)

            if len(t1) == 0 and len(t2) == 0:
                return []
            elif len(t1) != 0:
                t1.insert(0, root)
                return t1
            else:
                t2.insert(0, root)
                return t2

        l1 = getLines(root, p)
        l2 = getLines(root, q)

        for i in range(min(len(l1), len(l2))):
            if l1[i].val != l2[i].val:
                return l1[i - 1]

        return l1[len(min(l1, l2)) - 1]


if __name__ == "__main__":
    solution = Solution()
