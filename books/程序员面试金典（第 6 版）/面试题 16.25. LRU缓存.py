class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.data_dict = {}
        self.node_dict = {}
        self.node_list_head = Node(-1)
        self.node_list_tail = Node(-1)

        self.node_list_head.next = self.node_list_tail
        self.node_list_tail.prev = self.node_list_head

    def get(self, key: int) -> int:
        if key in self.data_dict:
            self._just_visit_it(key)
            return self.data_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self._just_visit_it(key)
        self.data_dict[key] = value

    def _just_visit_it(self, key):
        if key in self.data_dict:
            t = self.node_dict[key]

            # 删除一个元素
            t.prev.next = t.next
            t.next.prev = t.prev
        else:
            # 判断是否需要LRU，清除多余的元素
            if self.len == self.capacity:
                t = self.node_list_tail.prev
                t.prev.next = t.next
                t.next.prev = t.prev
                self.len -= 1
                del self.data_dict[t.val]
                del self.node_dict[t.val]
                del t

            self.len += 1
            # 获取需要新添加的节点
            t = Node(key)
            self.node_dict[key] = t

        # 新增到链表头
        t.next = self.node_list_head.next
        t.prev = self.node_list_head
        self.node_list_head.next = t
        t.next.prev = t


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def runTest():
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # 返回1
    cache.put(3, 3)  # 该操作会使得密钥2作废
    print(cache.get(2))  # 返回 - 1(未找到)
    cache.put(4, 4)  # 该操作会使得密钥1作废
    print(cache.get(1))  # 返回 - 1(未找到)
    print(cache.get(3))  # 返回3
    print(cache.get(4))  # 返回4

runTest()
