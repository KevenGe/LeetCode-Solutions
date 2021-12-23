from typing import List
import bisect


def bin_search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1


def bin_search_left_lt(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)

    while l <= r:
        m = (l + r) // 2
        if nums[m] >= target:
            if m == 0 or (m - 1 >= 0 and nums[m - 1] < target):
                return m
            else:
                r = m - 1
        elif nums[m] < target:
            l = m + 1
    return -1


def bin_search_left_le(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)

    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            if m == 0 or (m - 1 >= 0 and  nums[m - 1] <= target):
                return m
            else:
                r = m - 1
        elif nums[m] <= target:
            if m == len(nums) - 1:
                return m+1
            l = m + 1
    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 5]
    target = 5
    print(bisect.bisect(nums, target))
    print(bin_search_left_le(nums, target))

