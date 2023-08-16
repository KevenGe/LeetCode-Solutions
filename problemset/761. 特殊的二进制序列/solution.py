# 761. 特殊的二进制序列
# https://leetcode.cn/problems/special-binary-string/

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) == 0 or len(s) == 2:
            return s

        ans = []
        count = 0
        last_count_eq_zero_pos = -1
        for i, c in enumerate(s):
            if c == "1":
                count += 1
            elif c == "0":
                count -= 1

            if count == 0:
                ans.append("1" + self.makeLargestSpecial(s[last_count_eq_zero_pos + 2:i]) + "0")
                last_count_eq_zero_pos = i

        ans.sort(reverse=True)
        ans = "".join(ans)
        return ans


if __name__ == "__main__":
    so = Solution()

    assert so.makeLargestSpecial("11011000") == "11100100"
    assert so.makeLargestSpecial("10") == "10"
    assert so.makeLargestSpecial("1100") == "1100"
