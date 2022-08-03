# 556. 下一个更大元素 III
# https://leetcode.cn/problems/next-greater-element-iii/

from typing import List


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num_max = 2 ** 31 - 1
        num_min = 1

        def parse_n(n: int) -> List[int]:
            nums = []
            while n != 0:
                nums.append(n % 10)
                n = n // 10
            return nums

        nums = parse_n(n)

        up_num_idx = -1
        num_bef = 0
        for i in range(len(nums)):
            if nums[i] >= num_bef:
                num_bef = nums[i]
            else:
                up_num_idx = i
                break

        if up_num_idx == -1:
            return -1

        up_num_better_num = nums[up_num_idx]
        for i, num in enumerate(nums):
            if num > nums[up_num_idx]:
                up_num_better_num = i
                break

        nums[up_num_better_num], nums[up_num_idx] = nums[up_num_idx], nums[up_num_better_num]
        nums[0:up_num_idx] = sorted(nums[0:up_num_idx], reverse=True)

        n_n = 0
        for i, num in enumerate(nums):
            n_n += num * (10 ** i)

        if num_min <= n_n <= num_max:
            return n_n

        return -1


if __name__ == "__main__":
    so = Solution()
    assert so.nextGreaterElement(21) == -1
    assert so.nextGreaterElement(12) == 21
    assert so.nextGreaterElement(123) == 132
    assert so.nextGreaterElement(231) == 312
