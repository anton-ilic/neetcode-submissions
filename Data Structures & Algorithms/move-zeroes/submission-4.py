class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                continue
            nums[low] = nums[i]
            if low != i:
                nums[i] = 0
            low += 1
    
            
