class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for i in s: 
            counts[i] = counts.get(i, 0) + 1 
        
        for i in t:
            counts[i] = counts.get(i, 0) - 1
            if counts[i] < 0:
                return False 
                
        for key in s:
            if counts[key] != 0:
                return False 
        return True 