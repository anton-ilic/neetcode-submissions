class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # trie?

        # sort 
        words_sorted = sorted(words, key = lambda x : len(x), reverse = True)
        sol = ""
        ans = []
        for word in words_sorted:
            if word in sol:
                ans.append(word)
            else:
                sol = sol + " " + word
        return ans