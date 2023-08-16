from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:

        max_node_id = -1
        max_node_num = -1

        bian_ji_fen = [0] * len(edges)

        for i, edge in enumerate(edges):
            bian_ji_fen[edge] += i

        for i, b in enumerate(bian_ji_fen):
            if b > max_node_num:
                max_node_id = i
                max_node_num = b

        return max_node_id


if __name__ == "__main__":
    so = Solution()
    # assert so.edgeScore([1,0,0,0,0,7,7,5]) == 7
    # assert so.edgeScore([2,0,0,2]) == 0
    print(so.edgeScore([2, 0, 0, 2]))

