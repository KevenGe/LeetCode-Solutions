from typing import List

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        
        if n <= k:
            max_val = -1
            max_idx = -1
            for i, x in enumerate(skills):
                if x > max_val:
                    max_val = x
                    max_idx = i
            return max_idx
        
        l = 0
        r = 1
        t = 0
        
        while l < n and r < n:
            if skills[l] < skills[r]:
                l = r
                r = r + 1
                t = 1
            else:
                r = r + 1
                t += 1
            
            if t >= k:
                break
        
        return l