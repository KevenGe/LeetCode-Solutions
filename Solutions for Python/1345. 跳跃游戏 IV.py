# 1345. 跳跃游戏 IV
# https://leetcode-cn.com/problems/jump-game-iv/

from collections import deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        same_index = {}
        for i, a in enumerate(arr):
            if a in same_index:
                same_index[a].append(i)
            else:
                same_index[a] = [i]

        visited = set()
        que = deque()
        que.append((0, 0))

        while len(que) != 0:

            idx, step = que.popleft()
            visited.add(idx)

            if idx == len(arr) - 1:
                return step

            step += 1
            v = arr[idx]

            if v in same_index:
                for t in same_index[v]:
                    if t not in visited:
                        que.append((t, step))
                del same_index[v]

            if idx - 1 >= 0 and arr[idx] != arr[idx - 1] and idx - 1 not in visited:
                que.append((idx - 1, step))

            if (
                idx + 1 < len(arr)
                and arr[idx] != arr[idx + 1]
                and idx + 1 not in visited
            ):
                que.append((idx + 1, step))

