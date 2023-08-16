# 面试题 05.02. 二进制数转字符串
# https://leetcode-cn.com/problems/bianry-number-to-string-lcci/


class Solution:
    def printBin(self, num: float) -> str:
        ans = []
        hasError = True

        for i in range(32):
            if num == 0:
                hasError = False 
                break

            num = 2 * num
            if num >= 1:
                ans.append(1)
                num = num - 1
            else:
                ans.append(0)

        if hasError:
            return "ERROR"
        else:
            return "0."+"".join(map(str, ans))


if __name__ == "__main__":
    solution = Solution()
    print(solution.printBin(0.625))
