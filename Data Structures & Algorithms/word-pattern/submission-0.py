class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        mapping = {}
        for i in range(0, len(pattern)):
            if pattern[i] in mapping and mapping[pattern[i]] != s[i]:
                return False
            mapping[pattern[i]] = s[i]
        
        reverse_mapping = {}
        for i in range(0, len(pattern)):
            if s[i] in reverse_mapping and reverse_mapping[s[i]] != pattern[i]:
                return False
            reverse_mapping[s[i]] = pattern[i]
        return True

 