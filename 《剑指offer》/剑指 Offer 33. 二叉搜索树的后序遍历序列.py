# 剑指 Offer 33. 二叉搜索树的后序遍历序列
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/


from typing import List, Tuple


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def helper(
            postorder: List[int], left: int, right: int
        ) -> Tuple[bool, int, int]:  # isOK? max? min

            if left > right:
                return True, -float("inf"), float("inf")

            if left == right:
                return True, postorder[left], postorder[left]

            tar = postorder[right]
            m = left - 1
            for i in range(right - 1, left - 1, -1):
                if postorder[i] < tar:
                    m = i
                    break

            l = helper(postorder, left, m)
            r = helper(postorder, m + 1, right - 1)

            if l[0] == False or r[0] == False:
                return False, float("inf"), -float("inf")
            else:
                ans = tar > l[1] and tar < r[2]
                if ans:
                    return ans, max(l[1], r[1]), min(l[2], r[2])
                else:
                    return ans, float("inf"), -float("inf")
        
        t = helper(postorder, 0, len(postorder)-1)
        return t[0]

if __name__ == "__main__":
    solution = Solution()
