# 654. 最大二叉树
# https://leetcode.cn/problems/maximum-binary-tree/


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        m = nums.index(max(nums))
        return TreeNode(
            val=nums[m],
            left=self.constructMaximumBinaryTree(nums[:m]),
            right=self.constructMaximumBinaryTree(nums[m + 1 :]),
        )


if __name__ == "__main__":
    so = Solution()
    t = so.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    print(t)

