class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}
        total_words = len(words)
        for word in words:
            for letter in word:
                counts[letter] = counts.get(letter, 0) + 1
        
        for key in counts:
            if counts[key] % total_words != 0:
                return False
        return True