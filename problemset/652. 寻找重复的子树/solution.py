# 652. 寻找重复的子树
# https://leetcode.cn/problems/find-duplicate-subtrees/


from typing import Dict, Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __repr__(self) -> str:
    #     return "({})".format(self.val)


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:

        self.same: Dict[TreeNode, Dict[TreeNode, int]] = dict()
        self.all_set: Dict[int, List[TreeNode]] = dict()
        self.layer_set: Dict[int, List[TreeNode]] = dict()

        def add_same(tr1: TreeNode, tr2: TreeNode):
            if tr1 not in self.same:
                self.same[tr1] = dict()
            self.same[tr1][tr2] = 1

            if tr2 not in self.same:
                self.same[tr2] = dict()
            self.same[tr2][tr1] = 1

        def is_same(tr1: Optional[TreeNode], tr2: Optional[TreeNode]):
            if tr1 is None and tr2 is None:
                return True

            if (tr1 is not None and tr2 is None) or (tr1 is None and tr2 is not None):
                return False

            if tr1 not in self.same:
                return False
            if tr2 not in self.same[tr1]:
                return False
            return True

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return

            dfs(root.left)
            dfs(root.right)

            if root.left is None and root.right is None:
                if root.val not in self.layer_set:
                    self.layer_set[root.val] = []
                for other_treenode in self.layer_set[root.val]:
                    add_same(root, other_treenode)
                self.layer_set[root.val].append(root)

            else:
                if root.val not in self.all_set:
                    self.all_set[root.val] = []

                for other_treenode in self.all_set[root.val]:
                    if is_same(root.left, other_treenode.left) and is_same(
                        root.right, other_treenode.right
                    ):
                        add_same(root, other_treenode)

                self.all_set[root.val].append(root)

        dfs(root)

        def get_ans():
            need = set()
            un_need = set()
            for k, v in self.same.items():
                if k not in un_need:
                    need.add(k)
                    for u in v.keys():
                        un_need.add(u)

            return list(need)

        return get_ans()


if __name__ == "__main__":
    so = Solution()

    root1 = TreeNode(0)
    root2 = TreeNode(0, root1)
    root3 = TreeNode(0)
    root4 = TreeNode(0, root3)
    root5 = TreeNode(0, root2, root4)

    print(so.findDuplicateSubtrees(root5))
