# 911. 在线选举
# https://leetcode-cn.com/problems/online-election/


################################################################################

from typing import List
import bisect


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.best_person_by_time = []
        self.times = times.copy()

        tmp_times_dict = {}
        tmp_last_times_dict = {}
        for i in range(len(persons)):
            if persons[i] in tmp_times_dict:
                tmp_times_dict[persons[i]] += 1
            else:
                tmp_times_dict[persons[i]] = 1
            tmp_last_times_dict[persons[i]] = i

            best_person = -1
            best_times = -1
            for k, v in tmp_times_dict.items():
                if v > best_times:
                    best_person = k
                    best_times = v
                elif v == best_times:
                    if tmp_last_times_dict[k] > tmp_last_times_dict[best_person]:
                        best_person = k

            self.best_person_by_time.append(best_person)

    def q(self, t: int) -> int:
        t2 = bisect.bisect_right(self.times, t)

        t3 = self.best_person_by_time[t2 - 1]

        return t3


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

################################################################################
