class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        low = 0
        high = len(nums) - 1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
        
        low = 0
        high = k - 1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
        
        low = k
        high = len(nums) - 1
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1