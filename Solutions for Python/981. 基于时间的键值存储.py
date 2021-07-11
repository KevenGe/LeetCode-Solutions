# 981. 基于时间的键值存储
# https://leetcode-cn.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append({
                "timestamp": timestamp,
                "value": value
            })
        else:
            self.data[key] = [
                {
                    "timestamp": timestamp,
                    "value": value
                }
            ]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        # 最好的方式是采用二分查找z在有序列表找到内容
        l = 0
        r = len(self.data[key]) - 1
        li = self.data[key]

        while l <= r:
            m = (l+r) // 2
            if li[m]["timestamp"] <= timestamp:
                if m + 1 < len(li):
                    if li[m+1]["timestamp"] > timestamp:
                        break
                    else:
                        l = m+1
                else:
                    break
            else:
                r = m-1

        if l <= r:
            return li[m]["value"]
        else:
            return ""


if __name__ == "__main__":
    obj = TimeMap()
    obj.set("a", "aaa1", 1)
    obj.set("a", "aaa2", 12)
    obj.set("a", "aaa3", 13)
    obj.set("a", "aaa4", 123)
    print(obj.get("a", 123))

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
