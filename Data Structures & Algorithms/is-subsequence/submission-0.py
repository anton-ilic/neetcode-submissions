class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current = 0
        s_len = len(s)
        for i in range(0, len(t)):
            if current == s_len:
                return True

            if s[current] == t[i]:
                current += 1
        return current >= s_len
