class Solution:
    def hammingWeight(self, n: int) -> int:
        # can either 1. convert to binary
        count = 0
        while n != 0:
            if n % 2 != 0:
                count += 1
            n = n // 2
        return count