class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = {}
        for c in chars:
            counts[c] = counts.get(c, 0) + 1
        
        total = 0
        for word in words:
            word_counts = {}
            for c in word:
                word_counts[c] = word_counts.get(c, 0) + 1
            
            for c in word_counts.keys():
                if counts.get(c, 0) < word_counts.get(c, 0):
                    total -= len(word)
                    break
            total += len(word)
        
        return total