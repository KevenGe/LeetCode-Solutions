# 面试题 04.02. 最小高度树
# https://leetcode-cn.com/problems/minimum-height-tree-lcci/



# Definition for a binary tree node.
from typing import List
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def helper(l:int, r:int) -> TreeNode:
            if l > r :
                return None

            m =  math.ceil((l + r ) / 2)
            right_node = helper(m+1, r)
            left_node = helper(l, m-1)

            root_node = TreeNode(nums[m])
            root_node.left = left_node
            root_node.right = right_node
            return root_node

        return helper(0, len(nums)-1)

