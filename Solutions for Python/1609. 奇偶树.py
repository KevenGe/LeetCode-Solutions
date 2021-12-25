# 1609. 奇偶树
# https://leetcode-cn.com/problems/even-odd-tree/

# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        que = deque()
        que.append(root)

        isEven = True
        while len(que)!= 0:
            if isEven:
                next_que = deque()

                que_max = -1
                while len(que)!=0:
                    t = que.popleft()
                    if t.val %2 != 1:
                        return False
                    if t.val <= que_max:
                        return False
                    que_max = t.val

                    if t.left is not None:
                        next_que.append(t.left)
                    if t.right is not None:
                        next_que.append(t.right)
                que = next_que
                isEven = False
            else:
                next_que = deque()
                que_min = 1000000000
                while len(que) != 0:
                    t = que.popleft()
                    if t.val % 2 != 0:
                        return False
                    if t.val >= que_min:
                        return False
                    que_min = t.val
                    if t.left is not None:
                        next_que.append(t.left)
                    if t.right is not None:
                        next_que.append(t.right)
                que = next_que
                isEven = True
        return True

