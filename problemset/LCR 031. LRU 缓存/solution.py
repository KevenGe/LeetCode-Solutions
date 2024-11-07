from typing import Optional, Set, Dict


class CacheNode:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prior: CacheNode = None
        self.next: CacheNode = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = CacheNode(-1, -1)
        self.back = CacheNode(-1, -1)
        self.head.next = self.back
        self.back.prior = self.head
        self.key_set: Set[int] = set()
        self.key_dict: Dict[int, CacheNode] = dict()

    def get(self, key: int) -> int:
        if key not in self.key_set:
            return -1

        node = self.key_dict[key]
        node.prior.next = node.next
        node.next.prior = node.prior

        node.prior = self.head
        node.next = self.head.next
        self.head.next.prior = node
        self.head.next = node

        return self.head.next.val

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.head.next.val = value
            return

        node = CacheNode(key, value)
        node.prior = self.head
        node.next = self.head.next
        self.head.next.prior = node
        self.head.next = node
        self.count += 1
        self.key_set.add(key)
        self.key_dict[key] = node

        if self.count > self.capacity:
            node = self.back.prior
            node.prior.next = self.back
            self.back.prior = node.prior
            self.count -= 1
            self.key_set.remove(node.key)
            self.key_dict.pop(node.key)
            del node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
