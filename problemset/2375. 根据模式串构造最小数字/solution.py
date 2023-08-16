from typing import Dict, List


class Solution:
    def smallestNumber(self, pattern: str) -> str:

        d = dict([(i, False) for i in range(1, 10)])

        self.is_OK = False
        self.ans = ""

        def dfs(i: int, d: Dict[int, bool], tmp: List[int]):
            if i == len(pattern) + 1:
                self.is_OK = True
                self.ans = "".join(map(lambda x: str(x), tmp))
                return

            last_item = ""
            if i > 0:
                last_item = pattern[i - 1]

            for k, v in d.items():
                if v == False:
                    if (
                        (last_item == "")
                        or (last_item == "I" and k > tmp[-1])
                        or (last_item == "D" and k < tmp[-1])
                    ):
                        d[k] = True
                        tmp.append(k)
                        dfs(i + 1, d, tmp)
                        tmp.pop()
                        d[k] = False

                        if self.is_OK:
                            return

        dfs(0, d, [])
        return self.ans


if __name__ == "__main__":
    so = Solution()
    print(so.smallestNumber("DDD"))
    print(so.smallestNumber("IIIDIDDD"))
