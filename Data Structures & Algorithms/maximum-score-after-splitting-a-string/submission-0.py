class Solution:
    def maxScore(self, s: str) -> int:
        # count 0s and count 1s? 

        zeroes = 0

        for i in s:
            if i == "0":
                zeroes += 1
        
        ones = len(s) - zeroes

        seen_zeroes = 0
        right_ones = ones

        best = 0
        for left in range(0, len(s) - 1):
            # left is leftmost
            if s[left] == "0":
                seen_zeroes += 1
            else:
                right_ones -= 1
            best = max(seen_zeroes + right_ones, best)
        return best