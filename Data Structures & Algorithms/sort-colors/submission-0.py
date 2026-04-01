class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        for i in nums:
            if i == 0:
                r += 1
            elif i == 1:
                w += 1

        for i in range(0, r):
            nums[i] = 0
        
        for i in range(r, r + w):
            nums[i] = 1

        for i in range(r + w, len(nums)):
            nums[i] = 2
             