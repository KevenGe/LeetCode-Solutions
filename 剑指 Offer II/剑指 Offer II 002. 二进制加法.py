# 剑指 Offer II 002. 二进制加法
# https://leetcode.cn/problems/JFETK5/


# Python cheat version
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a, 2) + int(b, 2))[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(map(lambda x: int(x), list(a)))[::-1]
        b = list(map(lambda x: int(x), list(b)))[::-1]
        ans = []
        a_idx = 0
        b_idx = 0
        extra = 0
        while True:
            if a_idx < len(a) and b_idx < len(b):
                ans.append((a[a_idx] + b[b_idx] + extra) % 2)
                extra = (a[a_idx] + b[b_idx] + extra) // 2
                a_idx += 1
                b_idx += 1
            elif a_idx < len(a) and b_idx >= len(b):
                ans.append((a[a_idx] + extra) % 2)
                extra = (a[a_idx] + extra) // 2
                a_idx += 1
            elif a_idx >= len(a) and b_idx < len(b):
                ans.append((b[b_idx] + extra) % 2)
                extra = (b[b_idx] + extra) // 2
                b_idx += 1
            elif a_idx >= len(a) and b_idx >= len(b) and extra != 0:
                ans.append(1)
                break
            else:
                break
        return "".join(list(map(lambda x: str(x), ans[::-1])))


if __name__ == "__main__":
    so = Solution()
    print(so.addBinary("11", "10") == "101")
    print(so.addBinary("1010", "1011") == "10101")
    print(so.addBinary("0", "0") == "0")
