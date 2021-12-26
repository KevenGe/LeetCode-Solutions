# 5966. 还原原数组
# https://leetcode-cn.com/problems/recover-the-original-array/


from typing import List


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        nd = {}
        for num in nums:
            if num in nd:
                nd[num] += 1
            else:
                nd[num] = 1
        nd_keys = sorted(list(nd.keys()).copy())

        start = nums[0]

        for i in range(1, len(nums)):
            if (nums[i] - start) % 2 == 1 or nums[i] == start:
                continue
            m = nums[i] - start

            ndc = nd.copy()
            ans = []
            notOk = False
            for ndk in nd_keys:
                while ndc[ndk] != 0:
                    if ndk + m in ndc and ndc[ndk + m] != 0:
                        ndc[ndk + m] -= 1
                        ndc[ndk] -= 1
                        ans.append(ndk + m // 2)
                    else:
                        notOk = True
                        break
                if notOk:
                    break
            if notOk:
                continue
            else:
                return ans

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.recoverArray([5,435]))
