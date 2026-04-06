class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = nums[0]
        current = best
        for i in range(1, len(nums)):
            if nums[i] > nums[ i - 1]:
                current += nums[i]
            else:
                current = nums[i]
            best = max(best, current)
        return best