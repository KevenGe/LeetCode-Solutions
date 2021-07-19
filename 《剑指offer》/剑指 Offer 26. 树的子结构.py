# 剑指 Offer 26. 树的子结构
# https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def t(A, B):
            if A is None:
                if B is None:
                    return True
                else:
                    return False
            else:
                if B is None:
                    return True
                else:
                    if A.val != B.val:
                        return False
                    else:
                        return t(A.left, B.left) and t(A.right, B.right)

        return bool(A and B) and (
            t(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        )


if __name__ == "__main__":
    so = Solution()

    root1 = TreeNode(1)
    root2 = TreeNode(0)
    root3 = TreeNode(1)
    root4 = TreeNode(-4)
    root5 = TreeNode(3)

    root1.left = root2
    root1.right = root3
    root2.left = root4
    root2.right = root5

    root32 = TreeNode(1)
    root33 = TreeNode(-4)
    root32.left = root33

    print(so.isSubStructure(root1, root32))
