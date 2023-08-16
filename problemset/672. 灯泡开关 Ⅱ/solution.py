# 672. 灯泡开关 Ⅱ
# https://leetcode.cn/problems/bulb-switcher-ii/

from typing import List, Tuple


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = 5 if n > 5 else n
        presses = 9 if presses > 9 else presses

        d = set()

        def op(lights: List[bool], ops: Tuple[int, int, int]):
            lights = lights.copy()

            if ops[0] == 1:
                for i in [2, 4]:
                    if i < len(lights):
                        lights[i] = not lights[i]

            if ops[1] == 1:
                for i in [1, 3]:
                    if i < len(lights):
                        lights[i] = not lights[i]

            if ops[2] == 1:
                for i in [1, 4]:
                    if i < len(lights):
                        lights[i] = not lights[i]

            return lights

        for l1 in range(presses + 1):
            for l2 in range(presses + 1 - l1):
                for l3 in range(presses + 1 - l1 - l2):
                    l4 = presses - l1 - l2 - l3

                    l2 = l2 + l1
                    l3 = l3 + l1

                    l2 = l2 % 2
                    l3 = l3 % 2
                    l4 = l4 % 2

                    ops = (l2, l3, l4)
                    # print(ops)
                    res = str(op([False] * (n+1), ops))

                    d.add(res)

        # print(d)
        return len(d)


if __name__ == "__main__":
    so = Solution()
    # print(so.flipLights(1, 1))
    print(so.flipLights(2, 1))
    print(so.flipLights(3, 1))
