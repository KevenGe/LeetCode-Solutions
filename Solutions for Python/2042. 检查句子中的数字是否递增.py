# 2042. 检查句子中的数字是否递增
# https://leetcode-cn.com/problems/check-if-numbers-are-ascending-in-a-sentence/

################################################################################


class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        bfn = -1
        for t in s.split(" "):
            if t.isdigit():
                t = int(t)
                if t > bfn:
                    bfn = t
                else:
                    return False

        return True


################################################################################

if __name__ == "__main__":
    solution = Solution()
