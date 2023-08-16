# 654. 最大二叉树
# https://leetcode.cn/problems/maximum-binary-tree/


from typing import List, Optional, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
#         if len(nums) == 0:
#             return None

#         m = nums.index(max(nums))
#         return TreeNode(
#             val=nums[m],
#             left=self.constructMaximumBinaryTree(nums[:m]),
#             right=self.constructMaximumBinaryTree(nums[m + 1 :]),
#         )


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        s = []
        t: Dict[int, TreeNode] = dict()

        for num in nums:
            t[num] = TreeNode(val=num)
        
            l = -1
            while len(s) > 0 and num > s[-1]:
                p = s.pop()
                if l != -1:
                    t[p].right = t[l]
                l = p

            if l != -1:
                t[num].left = t[l]
            s.append(num)

        l = -1
        while len(s) > 0:
            p = s.pop()
            if l != -1:
                t[p].right = t[l]
            l = p

        return t[l]


if __name__ == "__main__":
    so = Solution()
    t = so.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    print(t)

