class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.cols = set()
        self.diag = set()
        self.bdiag = set()
        self.ans: int = 0
        self.dfs(0)

        return self.ans

    def dfs(self, row_idx: int):
        if row_idx == self.n:
            self.ans += 1
        else:
            for col_idx in range(self.n):
                if col_idx in self.cols:
                    continue

                diag_idx = row_idx - col_idx + (self.n - 1)
                if diag_idx in self.diag:
                    continue

                bdiag_idx = row_idx + col_idx
                if bdiag_idx in self.bdiag:
                    continue

                self.cols.add(col_idx)
                self.diag.add(diag_idx)
                self.bdiag.add(bdiag_idx)

                self.dfs(row_idx + 1)

                self.cols.remove(col_idx)
                self.diag.remove(diag_idx)
                self.bdiag.remove(bdiag_idx)
