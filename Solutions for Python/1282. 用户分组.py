# 1282. 用户分组
# https://leetcode.cn/problems/group-the-people-given-the-group-size-they-belong-to/


from typing import List, Dict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []

        tg: Dict[int, List[int]] = dict()
        for man_id, group_size in enumerate(groupSizes):
            if group_size not in tg:
                tg[group_size] = [man_id]
            else:
                tg[group_size].append(man_id)

            if len(tg[group_size]) == group_size:
                ans.append(tg[group_size])
                del tg[group_size]

        return ans
