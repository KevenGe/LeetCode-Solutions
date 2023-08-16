# 237. 删除链表中的节点
# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/

################################################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        targetNode = node.next
        node.val = targetNode.val
        node.next = targetNode.next

        del targetNode


################################################################################

if __name__ == "__main__":
    solution = Solution()

