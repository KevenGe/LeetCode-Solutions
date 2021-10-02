# 405. 数字转换为十六进制数
# https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/

################################################################################


def bin2hex(num: int) -> str:
    if num < 10:
        return str(num)
    elif num == 10:
        return "a"
    elif num == 11:
        return "b"
    elif num == 12:
        return "c"
    elif num == 13:
        return "d"
    elif num == 14:
        return "e"
    elif num == 15:
        return "f"
    else:
        return ""


class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"
        else:
            if num < 0:
                num = num & 0xFFFFFFFF
            ans = []
            while num != 0:
                a, b = divmod(num, 16)
                ans.append(bin2hex(b))
                num = a

            ans = "".join(reversed(ans))
            return ans


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.toHex(-1))

