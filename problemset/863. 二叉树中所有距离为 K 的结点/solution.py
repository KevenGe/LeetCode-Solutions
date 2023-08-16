# 863. 二叉树中所有距离为 K 的结点
# https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def initPars(root: TreeNode):
            ans = {}
            if root is None:
                return ans
            if root.left is not None:
                ans[root.left.val] = root
            if root.right is not None:
                ans[root.right.val] = root
            ans.update(initPars(root.left))
            ans.update(initPars(root.right))
            return ans

        pars = initPars(root)
        pars[root.val] = None

        def getTargetNode(root: TreeNode):
            if root is None:
                return None

            if root.val == target.val:
                return root

            l = getTargetNode(root.left)
            r = getTargetNode(root.right)

            if l is None:
                return r
            else:
                return l

        targetNode = getTargetNode(root)

        def getAns(node: TreeNode, f: TreeNode, depth: int):
            if node is None:
                return []

            if node.val == f.val:
                return []

            if depth == k:
                return [node.val]

            ans = []
            if node.left is not None and node.left.val != f.val:
                ans.extend(getAns(node.left, node, depth + 1))
            if node.right is not None and node.right.val != f.val:
                ans.extend(getAns(node.right, node, depth + 1))
            if pars[node.val] is not None and pars[node.val].val != f.val:
                ans.extend(getAns(pars[node.val], node, depth + 1))
            return ans

        ans = getAns(targetNode, TreeNode(-1), 0)
        return ans


if __name__ == "__main__":
    solution = Solution()
