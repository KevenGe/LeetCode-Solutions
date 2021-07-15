from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return i


if __name__ == "__main__":
    so = Solution()
    print(so.peakIndexInMountainArray([0, 2, 1, 0]))
