# 851. 喧闹和富有
# https://leetcode-cn.com/problems/loud-and-rich/

from typing import List, Dict


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_dict:Dict[int, List[int]] = {}
        for persion_id in range(len(quiet)):
            richer_dict[persion_id] = []
        for x,y in richer:
            richer_dict[y].append(x)

        ans = [-1 for i in range(len(quiet))]
        def dfs(person_id:int, ans:List[int]):
            if ans[person_id] == -1:
                ans[person_id] = person_id
                for x in richer_dict[person_id]:
                    dfs(x, ans)
                    if quiet[ans[x]] < quiet[ans[person_id]]:
                        ans[person_id] = ans[x]

        for person_id in range(len(quiet)):
            dfs(person_id,ans)
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.loudAndRich([[0,2],[1,2]],[0,1,2]))
