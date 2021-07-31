# 剑指 Offer 54. 二叉搜索树的第k大节点
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.ans = -1

        def mid(root:TreeNode):
            if root: 
                mid(root.right)

                self.k -= 1
                if self.k == 0:
                    self.ans = root.val
                
                mid(root.left)
        
        mid(root)
        return self.ans


if __name__ == "__main__":
    solution = Solution()
