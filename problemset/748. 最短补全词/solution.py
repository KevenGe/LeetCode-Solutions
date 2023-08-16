# 748. 最短补全词
# https://leetcode-cn.com/problems/shortest-completing-word/


from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        pattern = {}
        for l in licensePlate:
            if l.isalpha():
                if l.lower() in pattern:
                    pattern[l.lower()] += 1
                else:
                    pattern[l.lower()] = 1
        ans = None

        for word in words:
            t = pattern.copy()

            for w in word:
                if w in t:
                    t[w] -= 1

            isOk = True
            for k, v in t.items():
                if v > 0:
                    isOk = False
                    break
            if isOk is not True:
                continue

            if ans is None or len(word) < len(ans):
                ans = word

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestCompletingWord("GrC8950",["according","level","meeting","none","marriage","rest"]))
