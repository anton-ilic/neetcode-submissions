class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            key = ''.join(sorted(s))
            if anagrams.get(key, 0) == 0:
                anagrams[key] = []
            elems = anagrams[key]
            elems.append(s)
            anagrams[key] = elems
            
        return list(anagrams.values())