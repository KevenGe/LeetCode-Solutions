

class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n == 3:
              count += 2;
              break  
            elif n % 2 == 0:
                n = n // 2
            else:
                if n & 2:
                    n = n + 1
                else:
                    n = n - 1
            count += 1
        return count
