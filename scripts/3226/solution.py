class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        while n != k:
            l = n % 2
            r = k % 2
            if l != r:
                if l == 1 and r == 0:
                    ans += 1
                else:
                    return -1

            n = n // 2
            k = k // 2

        return ans
