import unittest


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ST = []
        TT = []
        for s in S:
            if s == "#":
                if len(ST) != 0:
                    ST.pop()
            else:
                ST.append(s)

        for s in T:
            if s == "#":
                if len(TT) != 0:
                    TT.pop()
            else:
                TT.append(s)

        return ST == TT


def runTest():
    so = Solution()
    assert so.backspaceCompare("y#fo##f", "y#f#o##f") == True


runTest()
