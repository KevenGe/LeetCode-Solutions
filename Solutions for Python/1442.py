from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        setss = dict()
        ans = 0
        for i in range(len(arr)):
            tmp = arr[i]
            for j in range(i + 1, len(arr)):
                tmp = tmp ^ arr[j]
                if tmp in setss:
                    ans += setss[tmp]
                    setss[tmp] += 1
                else:
                    setss[tmp] = 1
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.countTriplets([1, 1, 1, 1, 1]))
