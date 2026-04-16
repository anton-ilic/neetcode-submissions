class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for let in magazine:
            counts[let] = counts.get(let, 0) + 1
        
        for let in ransomNote:
            if let in counts:
                counts[let] = counts[let] - 1
                if counts[let] < 0:
                    return False
            else:
                return False
        return True