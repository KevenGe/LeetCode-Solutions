class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        zero_accu = [0] * len(s)
        zero_accu[0] = 1 if s[0] == "0" else 0
        for i in range(1, len(s)):
            zero_accu[i] = zero_accu[i - 1] + (1 if s[i] == "0" else 0)

        one_accu = [0] * len(s)
        one_accu[0] = 1 if s[0] == "1" else 0
        for i in range(1, len(s)):
            one_accu[i] = one_accu[i - 1] + (1 if s[i] == "1" else 0)

        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if i == 0:
                    a = zero_accu[j]
                    b = one_accu[j]
                else:
                    a = zero_accu[j] - zero_accu[i - 1]
                    b = one_accu[j] - one_accu[i - 1]

                if a <= k or b <= k:
                    ans += 1

        return ans
