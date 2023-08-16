# 剑指 Offer 32 - III. 从上到下打印二叉树 III
# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
from typing import List
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        q = Queue()
        q.put(root)
        count = 1
        nextLevelCount = 0
        tmpList = []
        curLevelNeedReversed = False
        while TreeNode:
            if count == 0:
                if curLevelNeedReversed:
                    ans.append(list(reversed(tmpList.copy())))
                else:
                    ans.append(tmpList.copy())
                curLevelNeedReversed = ~curLevelNeedReversed
                tmpList.clear()
                if nextLevelCount == 0:
                    break
                count = nextLevelCount
                nextLevelCount = 0
            else:
                t = q.get()
                tmpList.append(t.val)
                if t.left is not None:
                    q.put(t.left)
                    nextLevelCount += 1
                if t.right is not None:
                    q.put(t.right)
                    nextLevelCount += 1
                count -= 1
        return ans
