class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        current_sum = 0
        if total == 0:
            return 0 

        for i in range(0, len(nums)):
            if current_sum + current_sum + nums[i] == total:
                return i
            current_sum += nums[i]
            
        return -1
