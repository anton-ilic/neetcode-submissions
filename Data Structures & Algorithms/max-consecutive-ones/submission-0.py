class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        curr = 0
        for i in nums:
            if i == 0:
                best = max(best, curr)
                curr = 0
            else:
                curr += 1

        return max(best, curr)