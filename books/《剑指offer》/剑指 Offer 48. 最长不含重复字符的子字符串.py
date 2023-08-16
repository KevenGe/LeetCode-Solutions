# 剑指 Offer 48. 最长不含重复字符的子字符串
# https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        l = 0
        ans = 0
        for i, st in enumerate(s):
            if st in d:
                if d[st] >= l:
                    l = d[st] + 1
            d[st] = i
            ans = max(ans, i - l + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("a"))
