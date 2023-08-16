# 551. 学生出勤记录 I
# https://leetcode-cn.com/problems/student-attendance-record-i/


class Solution:
    def checkRecord(self, s: str) -> bool:
        aCount = 0
        freLate = 0
        for st in s:
            if st == "A":
                aCount += 1

            if st == "L":
                freLate += 1
                if freLate >= 3:
                    break
            else:
                freLate = 0

        return aCount < 2 and freLate < 3


if __name__ == "__main__":
    solution = Solution()
