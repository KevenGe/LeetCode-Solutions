class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        # 车
        if a == e and (
            c != e
            or (
                c == e
                and ((b < f and (d < b or d > f)) or (b > f and (d < f or d > b)))
            )
        ):
            return 1

        if b == f and (
            d != f
            or (
                d == f
                and ((a < e and (c < a or c > e)) or (a > e and (c < e or c > a)))
            )
        ):
            return 1

        if f - e == d - c and (
            f - e != b - a
            or ((c < e and (a < c or a > e)) or (c > e and (a < e or a > c)))
        ):
            return 1

        if f + e == d + c and (
            f + e != b + a
            or ((c < e and (a < c or a > e)) or (c > e and (a < e or a > c)))
        ):
            return 1

        return 2
