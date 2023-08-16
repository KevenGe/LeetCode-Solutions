# 剑指 Offer 37. 序列化二叉树
# https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "null"
        ans = []

        def dfs(root, ans):
            if root is not None:
                ans.append(root.val)
                dfs(root.left, ans)
                dfs(root.right, ans)
            else:
                ans.append("null")

        dfs(root, ans)
        return ",".join(list(map(str, ans)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ans = data.split(",")

        def trans(s: str):
            if s == "null":
                return None
            else:
                return TreeNode(int(s))

        ans = list(map(trans, ans))

        def dfs(ans, index):
            if ans[index] is not None:
                if ans[index + 1] is not None:
                    ans[index].left = ans[index + 1]
                    i = dfs(ans, index + 1)
                    ans[index].right = ans[i + 1]
                    i = dfs(ans, i + 1)
                    return i
                else:
                    if ans[index + 2] is not None:
                        ans[index].right = ans[index + 2]
                        i = dfs(ans, index + 2)
                        return i
                    else:
                        return index + 2
            else:
                return index

        dfs(ans, 0)
        return ans[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
