class Solution:
    def getSmallerWord(self, word_one, word_two, order_map):
        for i in range(0, len(word_one)):
            if i == len(word_two): # word2s is a prefix
                return word_two
            if order_map[word_one[i]] == order_map[word_two[i]]:
                continue
            elif order_map[word_one[i]] > order_map[word_two[i]]:
                return word_two
            else:
                return word_one
            # pairwise compare if DNE; 
        return word_one
       


    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}
        i = 0
        for letter in order:
            mapping[letter] = i
            i += 1

        for i in range(0, len(words) - 1):
            for j in range(i + 1, len(words)):
                if self.getSmallerWord(words[i], words[j], mapping) == words[j]:
                    return False
        return True
        
        