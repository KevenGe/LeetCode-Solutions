# KMP算法


class Solution:
    def find(self, s: str, t: str):
        next = self.initNext(t)

        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if j == -1 or s[i] == t[j]:
                i += 1
                j += 1
            else:
                j = next[j]

        return j == len(t)

    def initNext(self, t: str):
        """初始化Next数组（当不匹配的时候，需要挪动的数量）"""
        next = [-1] * len(t)

        if len(t) <= 2:
            return next

        for i in range(2, len(t)):
            if next[i - 1] == -1:
                if t[i - 1] == t[0]:
                    next[i] = 0
                else:
                    next[i] = -1
            else:
                j = next[i - 1]

                while j >= 0 and t[i - 1] != t[j]:
                    j = next[j - 1]

                if j >= 0:
                    next[i] = j + 1
                else:
                    next[i] = -1
        return next

    def initNext2(self, t: str):
        """初始化Next数组（当不匹配的时候，需要挪动的数量）"""
        next = [-1] * len(t)

        i = 0
        j = -1

        while i < len(t):
            if j == -1 or t[i - 1] == t[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
        return next


if __name__ == "__main__":
    so = Solution()
    print(so.find("abcdefghigklmn", "cd"))

