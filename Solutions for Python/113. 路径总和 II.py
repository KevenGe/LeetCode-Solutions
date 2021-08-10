# 113. 路径总和 II
# https://leetcode-cn.com/problems/path-sum-ii/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if root is None:
            return []

        ans = []

        def adds(root, curNum, tmpList, ans):
            if root.left is None and root.right is None:
                tmpList.append(root.val)
                curNum += root.val
                if curNum == target:
                    ans.append(copy.copy(tmpList))
                tmpList.pop()

            if root.left is not None:
                tmpList.append(root.val)
                adds(root.left, curNum + root.val, tmpList, ans)
                tmpList.pop()

            if root.right is not None:
                tmpList.append(root.val)
                adds(root.right, curNum + root.val, tmpList, ans)
                tmpList.pop()

        adds(root, 0, [], ans)

        return ans


if __name__ == "__main__":
    solution = Solution()
