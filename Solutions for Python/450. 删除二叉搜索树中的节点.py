# 450. 删除二叉搜索树中的节点
# https://leetcode.cn/problems/delete-node-in-a-bst/

from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key: int):

        def findNode(root, key: int):
            if root is not None:
                if root.val == key:
                    return None, root
                else:
                    a = (None, None)
                    if root.val < key:
                        a = findNode(root.right, key)
                    else:
                        a = findNode(root.left, key)
                    if a[1] is not None and a[0] is None:
                        a = (root, a[1])
                    return a
            else:
                return None, None

        par, node = findNode(root, key)
        if node is None:
            return root

        def mergeBinTree(left: TreeNode, right: TreeNode) -> TreeNode:
            if left is None:
                if right is None:
                    return None
                else:
                    return right
            else:
                if right is None:
                    return left
                else:
                    right.left = mergeBinTree(left, right.left)
                    return right

        if par is None:
            return mergeBinTree(node.left, node.right)
        else:
            if par.val > node.val:
                par.left = mergeBinTree(node.left, node.right)
            else:
                par.right = mergeBinTree(node.left, node.right)
            del node
            return root


if __name__ == "__main__":
    so = Solution()

    node5 = TreeNode(5)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node5.left = node3
    node3.left = node2
    node3.right = node4

    print(so.deleteNode(node5, 3))
