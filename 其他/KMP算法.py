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


class Solution2:
    def find(self, s: str, t: str):
        next = self.initNext(t)
        i = 0
        j = 0
        while True:
            if i == len(s):
                return False
            elif j == -1:
                i += 1
                j = 0
            elif j == len(t):
                return True
            else:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j = next[j]

    def initNext(self, t: str):
        next = [-1] * len(t)
        next[0] = -1

        for i in range(len(t) - 1):
            k = next[i]
            while True:
                if k == -1:
                    next[i + 1] = 0
                    break
                elif t[k] == t[i]:
                    next[i + 1] = k + 1
                    break
                else:
                    k = next[k]

        return next


class Solution3:
    def find(self, s: str, t: str):
        if t == "":
            return 0

        next = self.init_next(t)
        j = 0
        i = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j = next[j]
                if j == -1:
                    i += 1
                    j = 0

        return j == len(t)

    def init_next(self, t: str):
        next = [0] * len(t)
        next[0] = -1

        for i in range(2, len(t)):

            j = next[i - 1]
            while j != -1:
                if t[i - 1] == t[j]:
                    next[i] = next[i - 1] + 1
                    break
                else:
                    j = next[j]
        return next


if __name__ == "__main__":
    # so = Solution()
    # print(so.find("abcdefghigklmn", "cd"))
    # s2 = Solution2()
    # print(s2.find("abcdefghigklmn", "ebcd"))
    s2 = Solution2()
    print(s2.find("abcdefghigklmn", "igk"))
