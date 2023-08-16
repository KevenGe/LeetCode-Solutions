from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        n = len(A)
        dict1 = {}
        for i in A:
            for j in B:
                if i+j in dict1:
                    dict1[i+j] += 1
                else:
                    dict1[i+j] = 1

        for i in C:
            for j in D:
                if -i-j in dict1:
                    ans += dict1[-i-j]

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
