from typing import List


def bs(nums: List[int], tar: int) -> bool:
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] <= tar:
            l = m + 1
        else:
            r = m - 1
    return l


if __name__ == "__main__":
    print(bs([0, 0, 0, 1, 1, 1, 1, 2, 3, 4, 5], 1))

