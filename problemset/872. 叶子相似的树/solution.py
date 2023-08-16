from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getLayers(root: TreeNode) -> List[int]:
    ans = []

    def dfs(root: TreeNode):
        if root is None:
            return

        if root.left is None and root.right is None:
            ans.append(root.val)
        else:
            dfs(root.left)
            dfs(root.right)

    dfs(root)
    return ans


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return getLayers(root1) == getLayers(root2)

