# 589. N 叉树的前序遍历
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/


from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.a = []
        
        def dfs(root: 'Node'):
            if root is not None: 
                self.a.append(root.val) 
                for ch in root.children:
                    dfs(ch)
        dfs(root)
        return self.a

