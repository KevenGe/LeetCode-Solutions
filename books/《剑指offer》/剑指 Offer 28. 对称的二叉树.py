# 剑指 Offer 28. 对称的二叉树
# https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def dfs(rootA: TreeNode, rootB: TreeNode) -> bool:
            if rootA is None:
                if rootB is None:
                    return True
                else:
                    return False
            else:
                if rootB is None:
                    return False
                else:
                    if rootA.val == rootB.val:
                        return dfs(rootA.left, rootB.right) and dfs(
                            rootA.right, rootB.left
                        )
                    else:
                        return False

        return dfs(root.left, root.right)


if __name__ == "__main__":
    solution = Solution()
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(2)
    root4 = TreeNode(3)
    root5 = TreeNode(4)
    root1.left = root2
    root1.right = root3
    root2.right = root4
    root2.right = root5

    print(solution.isSymmetric(root1))