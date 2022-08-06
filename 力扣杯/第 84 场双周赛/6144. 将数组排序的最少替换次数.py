from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op_times = 0

        max_num = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > max_num:
                a, b = divmod(nums[i], max_num)
                if b == 0:
                    op_times += a - 1
                else:
                    op_times += a
                    a, b = divmod(nums[i], a + 1)
                    max_num = a
            else:
                max_num = nums[i]

        return op_times


if __name__ == "__main__":
    so = Solution()
    assert so.minimumReplacement([3, 9, 3]) == 2
    assert so.minimumReplacement([1, 2, 3, 4, 5]) == 0
    assert so.minimumReplacement([19, 7, 2, 24, 11, 16, 1, 11, 23]) == 73
