# 590. N 叉树的后序遍历
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/


from typing import List

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(root: Node, ans):
            if root:
                for chi in root.children:
                    dfs(chi, ans)
                ans.append(root.val)
        dfs(root, ans)
        return ans
