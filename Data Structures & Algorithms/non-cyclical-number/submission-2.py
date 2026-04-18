class Solution:
    def isHappy(self, n: int) -> bool:
        curr = n
        seen = set()
        
        while curr != 1:
            total = 0
            while curr != 0:
                total = (curr % 10) * (curr % 10) + total
                curr = curr // 10
            
            curr = total
            if curr in seen:
                return False
            seen.add(curr)
        
        return True
