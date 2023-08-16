# 面试题 04.03. 特定深度节点链表
# https://leetcode-cn.com/problems/list-of-depth-lcci/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        if tree is None:
            return ans

        que = [tree]
        while len(que) != 0:
            cur_listNode = None
            next_que = []
            for q in que:
                if cur_listNode is None:
                    cur_listNode = ListNode(q.val)
                    ans.append(cur_listNode)
                else:
                    tmp_listNode = ListNode(q.val)
                    cur_listNode.next = tmp_listNode
                    cur_listNode = tmp_listNode

                if q.left is not None:
                    next_que.append(q.left)
                if q.right is not None:
                    next_que.append(q.right)
            que = next_que

        return ans

