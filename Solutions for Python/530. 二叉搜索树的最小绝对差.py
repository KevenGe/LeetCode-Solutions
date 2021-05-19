
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = float("inf")
        self.par = -1
    
        def middleBianLi(self, root: TreeNode) -> None:
            if root is None:
                return
            middleBianLi(self, root.left)
            # print(root.val)
            
            if self.par != -1:
                self.ans = min(self.ans, abs(root.val - self.par))
            self.par = root.val

            middleBianLi(self, root.right)
    
        middleBianLi(self, root)
        return self.ans


def runTest():
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(2)
    a.right = b
    b.left = c
    
    S = Solution()
    print(S.getMinimumDifference(a))

runTest()
