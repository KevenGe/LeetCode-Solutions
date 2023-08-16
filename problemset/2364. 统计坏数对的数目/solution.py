from typing import List


# class Solution:
#     def countBadPairs(self, nums: List[int]) -> int:
#
#         ans = 0
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] - nums[i] != j - i:
#                     ans += 1
#         return ans


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] - i

        ans = 0
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                ans += i - d[nums[i]]
                d[nums[i]] += 1
            else:
                ans += i
                d[nums[i]] = 1
        return ans

if __name__ == "__main__":
    so = Solution()
    print(so.countBadPairs([4, 1, 3, 3]))
