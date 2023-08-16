# 1224. 最大相等频率
# https://leetcode.cn/problems/maximum-equal-frequency/

from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:

        max_freq = -1
        nums_freqs = dict()
        freqs_count = dict()

        ans = 1

        for i, num in enumerate(nums):

            if num in nums_freqs:
                freqs_count[nums_freqs[num]] -= 1
                nums_freqs[num] += 1

                if nums_freqs[num] in freqs_count:
                    freqs_count[nums_freqs[num]] += 1
                else:
                    freqs_count[nums_freqs[num]] = 1
            else:
                nums_freqs[num] = 1
                if 1 in freqs_count:
                    freqs_count[1] += 1
                else:
                    freqs_count[1] = 1

            max_freq = max(max_freq, nums_freqs[num])

            if max_freq == 1 and freqs_count[max_freq] * max_freq == i + 1:
                ans = i + 1
                continue

            if freqs_count[max_freq] * max_freq + 1 == i + 1 and freqs_count[1] == 1:
                ans = i + 1
                continue

            if (
                freqs_count[max_freq] == 1
                and freqs_count[max_freq - 1] * (max_freq - 1) + max_freq == i + 1
            ):
                ans = i + 1
                continue

        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.maxEqualFreq([2, 2, 1, 1, 5, 3, 3, 5]))
    print(so.maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))
