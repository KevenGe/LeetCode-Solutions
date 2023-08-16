# 剑指 Offer 43. 1～n 整数中 1 出现的次数
# https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/


class Solution:
    def countDigitOne(self, n: int) -> int:

        beforeLevelNumber = [0, 1]
        for i in range(10):
            t = beforeLevelNumber[-1]
            t = 10 ** (i + 1) + 10 * t
            beforeLevelNumber.append(t)
        # print(beforeLevelNumber)

        count = 0
        beforeAllNumber = 0
        for i, num in enumerate(reversed(list(str(n)))):
            # print(i)
            if num >= "2":
                count += int(num) * beforeLevelNumber[i]
                count += 10 ** i
            elif num == "1":
                count += beforeAllNumber + 1
                count += beforeLevelNumber[i]
            else:
                pass
            beforeAllNumber = beforeAllNumber + int(num) * (10 ** i)
        return count


if __name__ == "__main__":
    solution = Solution()
