# 559. N 叉树的最大深度
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/

################################################################################
from functools import reduce

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        else:
            return reduce(lambda x,y: max(x, self.maxDepth(y)), root.children, 0) + 1

################################################################################

