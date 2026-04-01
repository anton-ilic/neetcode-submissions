from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # pretty sure u can brute the paths OR this could be a math problem?

        # is this m choose n?

        # there are m - 1 down moves and n - 1 right moves

        # m + n - 2 moves total
        # m + n - 2 choose (m - 1)
        return comb(m + n - 2, m - 1)