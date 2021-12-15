# 面试题 04.04. 检查平衡性
# https://leetcode-cn.com/problems/check-balance-lcci/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def get_node_height(root: TreeNode) -> int:
            if root is None:
                return 0
            left_node_height = get_node_height(root.left)
            right_node_height = get_node_height(root.right)

            if left_node_height == -1 or right_node_height == -1 or abs(left_node_height - right_node_height) > 1:
                return -1
            else:
                return max(left_node_height, right_node_height) + 1

        return get_node_height(root) != -1
