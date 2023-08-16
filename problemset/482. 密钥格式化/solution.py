# 482. 密钥格式化
# https://leetcode-cn.com/problems/license-key-formatting/

################################################################################


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = list()
        cnt = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                ans.append(s[i].upper())
                cnt += 1
                if cnt % k == 0:
                    ans.append("-")

        if ans and ans[-1] == "-":
            ans.pop()

        return "".join(ans[::-1])


################################################################################


if __name__ == "__main__":
    solution = Solution()
    print(solution.licenseKeyFormatting("5F3Z-2e-9-w", 4))
