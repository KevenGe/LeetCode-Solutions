from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:

        winner = set()
        player_dict = dict()
        for x, y in pick:
            if x not in player_dict:
                player_dict[x] = dict()
            if y not in player_dict[x]:
                player_dict[x][y] = 0
            player_dict[x][y] += 1
            if player_dict[x][y] > x:
                winner.add(x)
        return len(winner)
