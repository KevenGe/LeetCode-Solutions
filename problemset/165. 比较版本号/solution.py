# 165. 比较版本号
# https://leetcode-cn.com/problems/compare-version-numbers/


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        m = max(len(v1), len(v2))

        for i in range(m):
            if i < len(v1):
                t1 = int(v1[i])
            else:
                t1 = 0
            if i < len(v2):
                t2 = int(v2[i])
            else:
                t2 = 0

            if t1 > t2:
                return 1
            elif t1 < t2:
                return -1
        return 0


if __name__ == "__main__":
    solution = Solution()
