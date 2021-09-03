# 面试题 17.14. 最小K个数
# https://leetcode-cn.com/problems/smallest-k-lcci/

from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        ans = []
        self.fastSort(arr, k, 0, len(arr) - 1)

        for i in range(k):
            ans.append(arr[i])

        return ans

    def fastSort(self, arr: List[int], k, left, right):
        if k == 0 or right - left <= 0:
            return
        elif right - left == 1:
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
        else:
            l = left
            r = right
            m = right

            while l < r:
                while l < r and arr[l] <= arr[m]:
                    l += 1
                while l < r and arr[r] >= arr[m]:
                    r -= 1

                if l != r:
                    arr[l], arr[r] = arr[r], arr[l]

            arr[l], arr[m] = arr[m], arr[l]
            self.fastSort(arr, k, left, l - 1)
            if l <= k - 2:
                self.fastSort(arr, k, l + 1, right)


if __name__ == "__main__":
    solution = Solution()
