from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


##############################################################################

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stacks=[]

        r = root

        while len(stacks) !=0 or r is not None:
            while r is not None:
                stacks.append(r)
                r = r.left
            r = stacks.pop()
            ans.append(r.val)
            r = r.right
        return ans

##############################################################################

def runTest():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.right = b
    b.left = c

    so = Solution()
    print(so.inorderTraversal(a))

runTest()
