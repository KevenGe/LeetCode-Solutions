from typing import List, Optional


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:

        INT_MIN = int(-1e10)

        class TNode:
            def __init__(self, val: int = INT_MIN) -> None:

                self.left_idx = -1
                self.right_idx = -1
                self.mid_idx = -1

                self.t00 = 0
                self.t01 = 0
                self.t10 = 0
                self.t11 = val

                self.parent: Optional[TNode] = None
                self.left_node: Optional[TNode] = None
                self.right_node: Optional[TNode] = None

        def update_tnode(self: TNode) -> None:
            if self.left_node is None or self.right_node is None:
                return

            self.t00 = max(
                self.left_node.t00 + self.right_node.t00,
                self.left_node.t00 + self.right_node.t10,
                self.left_node.t01 + self.right_node.t00,
            )
            self.t01 = max(
                self.left_node.t00 + self.right_node.t01,
                self.left_node.t00 + self.right_node.t11,
                self.left_node.t01 + self.right_node.t01,
            )
            self.t10 = max(
                self.left_node.t10 + self.right_node.t00,
                self.left_node.t10 + self.right_node.t10,
                self.left_node.t11 + self.right_node.t00,
            )
            self.t11 = max(
                self.left_node.t10 + self.right_node.t01,
                self.left_node.t10 + self.right_node.t11,
                self.left_node.t11 + self.right_node.t01,
            )

        id_tnode_map = [TNode()] * len(nums)

        def create_tnodes(nums: List[int], l: int = -1, r: int = -1) -> TNode:
            if l == -1:
                l = 0
            if r == -1:
                r = len(nums) - 1

            n = r - l + 1

            if n == 1:
                id_tnode_map[l] = TNode(nums[l])
                return id_tnode_map[l]

            for i in range(100):
                if 2**i >= n:
                    m = l + 2 ** (i - 1)
                    break

            ans = TNode()

            ans.left_idx = l
            ans.right_idx = r
            ans.mid_idx = m

            ans.left_node = create_tnodes(nums, l, m - 1)
            ans.left_node.parent = ans

            ans.right_node = create_tnodes(nums, m, r)
            ans.right_node.parent = ans

            update_tnode(ans)
            

            return ans

        head = create_tnodes(nums)

        MOD = int(1e9 + 7)

        ans = 0
        for x, y in queries:
            tnode = id_tnode_map[x]
            tnode.t11 = y
            
            while tnode is not None:
                update_tnode(tnode)
                tnode = tnode.parent
            
            ans = (ans +  max(head.t00, head.t01, head.t10, head.t11)) % MOD
            
        return ans


# so = Solution()
# print(so.maximumSumSubsequence([3, 5, 9], [[1, -2], [0, -3]]))
# print(so.maximumSumSubsequence([0,-1], [[0,-5]]))
