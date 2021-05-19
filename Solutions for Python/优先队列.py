from queue import PriorityQueue


class NT():
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return self.a < other.a

    def __str__(self):
        return str(self.a)

q = PriorityQueue()
q.put(NT(2))
q.put(NT(1))
q.put(NT(4))
q.put(NT(-8))

while q.empty() == False:
    print(q.get())
