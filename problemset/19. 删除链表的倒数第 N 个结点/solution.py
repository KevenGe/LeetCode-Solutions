# class Solution:
#     def minimumOperations(self, leaves: str) -> int:
#         dp = [[0, 0, 0] for i in range(len(leaves))]

#         dp[0][0] = 0 if leaves[0] == 'r' else 1
#         for i in range(1, len(leaves)):
#             dp[i][0] = dp[i-1][0] + (0 if leaves[i] == 'r' else 1)

#         dp[0][1] = float('inf')
#         for i in range(1, len(leaves)):
#             dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + \
#                 (0 if leaves[i] == 'y' else 1)

#         dp[0][2] = float('inf')
#         dp[1][2] = float('inf')
#         for i in range(2, len(leaves)):
#             dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + \
#                 (0 if leaves[i] == 'r' else 1)

#         return dp[len(leaves)-1][2]

class Solution:
    def minimumOperations(self, leaves: str) -> int:
        dp = [self.isRed(leaves[0]), float("inf"), float("inf")]

        for i in range(1, len(leaves)):
            if i >= 2:
                dp[2] = min(dp[1], dp[2]) + self.isRed(leaves[i])
            dp[1] = min(dp[0], dp[1]) + self.isYellow(leaves[i])
            dp[0] = dp[0] + self.isRed(leaves[i])
        return dp[2]

    def isRed(self, ch):
        return 0 if ch == 'r' else 1

    def isYellow(self, ch):
        return 0 if ch == 'y' else 1


def runTest():
    t = Solution()
    print(t.minimumOperations("yry"))

if __name__ == "__main__":
    runTest()
