class Solution:
    def isMonotonicIncreasing(self, nums):
        prev = nums[0]
        for i in nums:
            if i >= prev:
                prev = i
            else:
                return False
        return True
    
    def isMonotonicDecreasing(self, nums):
        prev = nums[0]
        for num in nums:
            if num <= prev:
                prev = num
            else:
                return False
        return True

    def isMonotonic(self, nums: List[int]) -> bool:
        return self.isMonotonicIncreasing(nums) or self.isMonotonicDecreasing(nums)