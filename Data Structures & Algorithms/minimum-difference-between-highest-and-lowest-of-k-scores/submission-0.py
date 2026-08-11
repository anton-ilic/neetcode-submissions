class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # then choose high, low
        low = 0
        high = k - 1
        best = float('inf')
        while high < len(nums):
            if nums[high] - nums[low] < best:
                best = nums[high] - nums[low]
            high += 1
            low += 1
        return best
