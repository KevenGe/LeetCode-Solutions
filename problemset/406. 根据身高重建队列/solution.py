from typing import List
import functools


def cmps(a,b):
    if a[0] > b[0]:
        return -1
    elif a[0] == b[0]:
        if a[1] < b[1]:
            return -1
        else:
            return 1
    else:
        return 1

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=functools.cmp_to_key(cmps))
        # print(people)
        for i in range(len(people)):
            num = 0
            if num == people[i][1]:
                # 移除
                t = people.pop(i)
                people.insert(0, t)
                continue
            for j in range(0, i):
                if people[j][0] >= people[i][0]:
                    num += 1
                if num == people[i][1]:
                    # 移除
                    t = people.pop(i)
                    people.insert(j+1, t)
                    break
        return people

s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))