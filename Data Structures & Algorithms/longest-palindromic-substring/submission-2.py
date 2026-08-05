class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(0, len(s)):
            # check if is odd centered here; check if is even center here
            # odd
            low = i
            high = i
            while low >= 0 and high < len(s):
                if s[low] == s[high]:
                    if high - low + 1 > len(ans):
                        ans = s[low:high + 1]
                else:
                    break
                low -= 1
                high += 1
            
            # even
            low = i
            high = i + 1
            while low >= 0 and high < len(s):
                if s[low] == s[high]:
                    if high - low + 1 > len(ans):
                        ans = s[low:high + 1]
                else:
                    break
                low -= 1
                high += 1
        return ans
            

