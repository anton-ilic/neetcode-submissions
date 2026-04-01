class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] != s[high]:
                s_without_low = s[:low] + s[low + 1:]
                s_without_high = s[:high] + s[high + 1:]
                return self.is_palindrome(s_without_low) or self.is_palindrome(s_without_high)
            low += 1
            high -= 1
        return True
