class Solution:
    def longestCommon(self, s1, s2):
        min_length = min(len(s1), len(s2))
        best = []
        for i in range(0, min_length):
            if s1[i] == s2[i]:
                best.append(s1[i])
            else:
                if len(best) == 0:
                    return ''
                return ''.join(best)
        if len(best) == 0:
            return ''
        return ''.join(best)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # backtrack? 
        longest = strs[0]
        for i in range(1, len(strs)):
            longest = self.longestCommon(longest, strs[i])
        return longest
            

