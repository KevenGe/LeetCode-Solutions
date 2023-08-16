from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        days = 0

        cur_day = 1

        last_task_day = dict()
        for task in tasks:
            if task not in last_task_day:
                last_task_day[task] = cur_day
                cur_day += 1
                continue
            else:
                if cur_day - last_task_day[task] >= space + 1:
                    last_task_day[task] = cur_day
                    cur_day += 1
                    continue
                else:
                    cur_day = last_task_day[task] + space + 1
                    last_task_day[task] = cur_day
                    cur_day += 1
                    continue

        cur_day -= 1

        return cur_day


if __name__ == "__main__":
    so = Solution()
    assert so.taskSchedulerII([1, 2, 1, 2, 3, 1], 3) == 9
    assert so.taskSchedulerII([5,8,8,5],2) == 6