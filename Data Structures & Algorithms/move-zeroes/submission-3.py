class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        for i in range(0, len(nums) - low):
            if nums[i] == 0:
                continue
            nums[low] = nums[i]
            low += 1
        
        for i in range(low, len(nums)):
            nums[i] = 0
        
             
            
