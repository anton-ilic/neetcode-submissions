class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # sorted anagram letterwise => anagrams
        for anagram in strs:
            ana = list(anagram)
            key = ''.join(sorted(ana))

            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(anagram)
        return list(anagrams.values())
        