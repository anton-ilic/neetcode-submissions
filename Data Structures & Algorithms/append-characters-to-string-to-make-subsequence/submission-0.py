class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        low_t = 0
  
        max_s = len(s)
        max_t = len(t)
        for i in range(0, max_s):
            if t[low_t] == s[i]:
                low_t += 1
            
            if low_t == max_t:
                return 0
        # there are low_s characters of s in the string
        # there needs to be len(s) - low_s?
        return max_t - low_t
        