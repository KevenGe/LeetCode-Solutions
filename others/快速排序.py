# 快速排序
# 2021-09-03


from typing import List


class Solution:
    def sort(self, arr: List[int], left, right):
        # 快速排序
        # 采用递归的方式进行书写

        if right - left <= 0:
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
                else:
                    break

            arr[l], arr[m] = arr[m], arr[l]
            self.sort(arr, left, l - 1)
            self.sort(arr, l + 1, right)


if __name__ == "__main__":
    solution = Solution()
    t = [1, 124, -123, 123, -1]
    solution.sort(t, 0, len(t) - 1)
    print(t)
