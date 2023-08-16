# 1583. 统计不开心的朋友
# https://leetcode-cn.com/problems/count-unhappy-friends/

from typing import List


class Solution:
    def unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]]
    ) -> int:
        isUnhappys = [False] * n
        dp = [[0 for j in range(n)] for i in range(n)]
        for i, preference in enumerate(preferences):
            for j, p in enumerate(preference, 1):
                dp[i][p] = -j

        # print(dp)

        uMap = {}
        for pair in pairs:
            uMap[pair[0]] = pair[1]
            uMap[pair[1]] = pair[0]
        # print(uMap)

        for i in range(n):
            for t in preferences[i]:
                if t != uMap[i]:
                    if dp[t][i] > dp[t][uMap[t]]:
                        isUnhappys[i] = True
                        isUnhappys[t] = True
                else:
                    break

        count = 0
        for isUnhappy in isUnhappys:
            if isUnhappy:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.unhappyFriends(
            4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]]
        )
    )

