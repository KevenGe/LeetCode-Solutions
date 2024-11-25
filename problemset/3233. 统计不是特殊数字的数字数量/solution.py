from math import sqrt, floor, ceil


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:

        nl = sqrt(l)
        nr = sqrt(r)

        prime_number = [True] * (floor(nr) + 1)
        for i in range(2, floor(nr) + 1):
            if prime_number[i]:
                for z in range(i * 2, int(nr) + 1, i):
                    prime_number[z] = False
            else:
                continue

        ans = 0
        for i in range(max(ceil(nl), 2), floor(nr) + 1):
            if prime_number[i]:
                ans += 1
        ans = (r - l + 1) - ans

        return ans
