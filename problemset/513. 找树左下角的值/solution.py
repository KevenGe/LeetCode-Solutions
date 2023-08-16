# 513. 找树左下角的值
# https://leetcode.cn/problems/find-bottom-left-tree-value/


from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode]) -> Tuple[int, int]:
            if root:
                lv, ld = dfs(root.left)
                rv, rd = dfs(root.right)

                if ld == 0:
                    if rd == 0:
                        return root.val, 1
                    else:
                        return rv, rd + 1
                else:
                    if rd == 0:
                        return lv, ld + 1
                    else:
                        if ld >= rd:
                            return lv, ld + 1
                        else:
                            return rv, rd + 1
            else:
                return -1, 0

        rv, rd = dfs(root)
        return rv
