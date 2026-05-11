class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # find two largest and 2 smallest
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]