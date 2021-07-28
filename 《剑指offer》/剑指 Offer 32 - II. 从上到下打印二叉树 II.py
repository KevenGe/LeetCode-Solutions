# 剑指 Offer 32 - II. 从上到下打印二叉树 II
# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/


from typing import List
import queue

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
        q = queue.Queue()
        count = 1
        q.put(root)

        ans = []
        while True:
            nextLevelCount = 0
            tmp = []
            while count != 0:
                t = q.get()
                tmp.append(t.val)
                if t.left is not None:
                    q.put(t.left)
                    nextLevelCount += 1
                if t.right is not None:
                    q.put(t.right)
                    nextLevelCount += 1
                count -= 1
            ans.append(tmp)
            if nextLevelCount == 0:
                break
            else:
                count = nextLevelCount
        return ans


if __name__ == "__main__":
    solution = Solution()
