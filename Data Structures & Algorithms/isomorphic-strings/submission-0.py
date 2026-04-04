class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.isIsomorphicHelper(s, t) and self.isIsomorphicHelper(t, s)

    def isIsomorphicHelper(self, s, t):
        if len(s) != len(t):
            return False 

        char_map = {}
        for i in range(0, len(s)):
            if s[i] in char_map and char_map[s[i]] != t[i]:
                return False
            char_map[s[i]] = t[i]

        return True
    