# 剑指 Offer 32 - I. 从上到下打印二叉树
# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
from queue import Queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        q = Queue()
        q.put(root)
        ans = []
        while q.empty() != True:
            t = q.get()
            ans.append(t.val)
            if t.left is not None:
                q.put(t.left)
            if t.right is not None:
                q.put(t.right)
        return ans


if __name__ == '__main__':
    solution = Solution()
