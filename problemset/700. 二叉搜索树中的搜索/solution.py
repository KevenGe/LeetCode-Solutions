# 700. 二叉搜索树中的搜索
# https://leetcode-cn.com/problems/search-in-a-binary-search-tree/

################################################################################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None

        if root.val == val:
            return root
        else:
            if root.val < val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)


################################################################################

if __name__ == "__main__":
    solution = Solution()
