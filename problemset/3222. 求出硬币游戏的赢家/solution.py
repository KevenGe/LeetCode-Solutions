class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        a = "Alice"
        b = "Bob"

        cur_is_a = True
        while True:
            if not (x >= 1 and y >= 4):
                break

            cur_is_a = not cur_is_a
            x = x - 1
            y = y - 4
    
        return b if cur_is_a else a
