from queue import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        queue = deque()
        queue.append(node)

        while len(queue) != 0:
            t = queue.popleft()
            n = Node(t.val)
            visited[t] = n

            for neighbor in t.neighbors:
                if neighbor in visited:
                    n.neighbors.append(visited[neighbor])
                else:
                    queue.append(neighbor)
                    t = Node(neighbor.val)
                    visited[neighbor] = t
                    n.neighbors.append(t)
        return visited[node]