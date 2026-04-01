class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                continue
            nums[current] = nums[i]
            if current != i:
                nums[i] = 0
            current += 1
        
        # for i in range(len(nums) - current, len(nums)):
        #     nums[i] = 0
        