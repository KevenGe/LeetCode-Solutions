# 剑指 Offer 36. 二叉搜索树与双向链表
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        def mid(root):
            if root.left:
                first, t = mid(root.left)
                t.right = root
                root.left = t
            else:
                first = root

            if root.right:
                t, end = mid(root.right)
                root.right = t
                t.left = root
            else:
                end = root

            return first, end

        if root is None:
            return None
        first, end = mid(root)
        first.left = end
        end.right = first
        return first


if __name__ == "__main__":
    root1 = Node(1)
    root2 = Node(2)
    root3 = Node(3)
    root4 = Node(4)
    root5 = Node(5)

    root4.left = root2
    root4.right = root5
    root2.left = root1
    root2.right = root3

    solution = Solution()
    print(solution.treeToDoublyList(root4))
