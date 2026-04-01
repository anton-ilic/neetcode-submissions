class Solution:
    def is_valid(self, s):
        low = 0
        high = len(s) - 1
        while low < high:
            while not s[low].isalnum() and low < high:
                low += 1

            while not s[high].isalnum() and low < high:
                high -= 1
    
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        while low < high:
            while not s[low].isalnum() and low < high:
                low += 1

            while not s[high].isalnum() and low < high:
                high -= 1
    
            if s[low].lower() != s[high].lower():
                return self.is_valid(s[:low] + s[low + 1:]) or self.is_valid(s[:high] + s[high + 1:])
            low += 1
            high -= 1
        return True