class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_map = {}
        low = 0
        best = 0
        for i in range(0, len(s)):
            charAt = s[i]
            if charAt in character_map:
                low = max(character_map[charAt] + 1, low)
            # else:
            character_map[charAt] = i
            best = max(best, i - low + 1)
        return best

