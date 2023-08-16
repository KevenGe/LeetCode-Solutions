# 636. 函数的独占时间
# https://leetcode.cn/problems/exclusive-time-of-functions/

from typing import List,Tuple


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        st = []
        func_costs = [0] * n

        def parse_log(log:str) -> Tuple[int, str, int]:
            func_id, status, time_step = log.split(":")
            func_id = int(func_id)
            time_step = int(time_step)
            return func_id, status, time_step

        for log in logs:
            func_id, status, time_step = parse_log(log)

            if status == "start":
                if len(st) != 0:
                    last_func_id, last_time_step = st[-1]
                    func_costs[last_func_id] += time_step - last_time_step
                st.append((func_id, time_step))
            elif status == "end":
                last_func_id, last_time_step = st.pop()
                func_costs[last_func_id] += time_step - last_time_step + 1

                if len(st) != 0:
                    st[-1] = (st[-1][0], time_step + 1)
        return func_costs


if __name__ == "__main__":
    so = Solution()
    print(so.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
    print(so.exclusiveTime(1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]))
    print(so.exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]))
    print(so.exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"]))
    print(so.exclusiveTime(1, ["0:start:0", "0:end:0"]))
