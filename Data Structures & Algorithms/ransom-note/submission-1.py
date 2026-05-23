class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransdomNote
        # maganize: 
        # return true iof randomnote can be made from letters in maganaize 
        counts = {}
        for letter in ransomNote:
            counts[letter] = counts.get(letter, 0) + 1
        
        for letter in magazine:
            if letter in counts:
                counts[letter] = counts[letter] - 1
        
        for count in counts.values():
            if count > 0:
                return False
        return True