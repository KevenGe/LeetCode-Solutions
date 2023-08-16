# 768. 最多能完成排序的块 II
# https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/

from typing import List, Dict


# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         """普通遍历解法"""
#         arrs = sorted(arr)
#         nexti: Dict[int, int] = dict()
#         for i, a in enumerate(arrs):
#             if a not in nexti:
#                 nexti[a] = i

#         ri = 0
#         m = -1
#         mi = 0
#         count = 0

#         for ai, a in enumerate(arr):
#             if nexti[a] > ri:
#                 ri = nexti[a]

#             if a == m:
#                 mi += 1
#                 ri += 1
#             elif a > m:
#                 m = a
#                 mi = 1

#             if ai == ri:
#                 count += 1
#                 ri = ai + 1
#                 m = -1
#                 mi = 0

#         return count



class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """单调栈解法"""
        st = []

        count = 0

        for a, b in zip(arr, sorted(arr)):
            if len(st) == 0:
                st.append(a)
            else:
                if st[-1] > a:
                    pass
                elif st[-1] == a:
                    st.append(a)
                elif st[-1] < a:
                    st = [a]

            if st[-1] == b:
                st.pop()
                if len(st) == 0:
                    count += 1

        return count


if __name__ == "__main__":
    so = Solution()
    assert so.maxChunksToSorted([5, 4, 3, 2, 1]) == 1
    assert so.maxChunksToSorted([2, 1, 3, 4, 4]) == 4
    assert so.maxChunksToSorted([1, 1, 0, 0, 1]) == 2

