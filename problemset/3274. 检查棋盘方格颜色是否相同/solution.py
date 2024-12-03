class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def get_color(coor: str) -> int:
            return ((ord(coor[0]) - ord("a")) + ord(coor[1])) % 2

        return get_color(coordinate1) == get_color(coordinate2)
