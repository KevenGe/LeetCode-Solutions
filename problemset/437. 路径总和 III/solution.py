# 437. 路径总和 III
# https://leetcode-cn.com/problems/path-sum-iii/

################################################################################


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        self.count = 0

        def mergeAB(l: dict, r: dict) -> dict:
            t = l.copy()
            for k, v in r.items():
                if k in t:
                    t[k] += v
                else:
                    t[k] = v
            return t

        def help(root: TreeNode) -> dict:
            if root is None:
                return {}

            l = help(root.left)
            r = help(root.right)
            t = mergeAB(l, r)

            if root.val == targetSum:
                self.count += 1

            if targetSum - root.val in t:
                self.count += t[targetSum - root.val]

            t2 = {}
            for k, v in t.items():
                t2[k + root.val] = v
            t = t2

            if root.val in t:
                t[root.val] += 1
            else:
                t[root.val] = 1

            return t

        help(root)
        return self.count


################################################################################


if __name__ == "__main__":
    solution = Solution()

    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)

    # root1.left = root2
    # root1.right = root3

    print(solution.pathSum(root1, 1))
