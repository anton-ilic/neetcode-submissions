class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # check if sum(nums) >= target; if not, return 0
        if sum(nums) < target:
            return 0
    
        # 1000 , 0, 0, 999, 999
        min_length = len(nums)

        current_sum = 0
        low = 0
        for current_index in range(0, len(nums)):
            current_sum += nums[current_index]
            while current_sum >= target:
                min_length = min(min_length, current_index - low + 1)
                current_sum -= nums[low]
                low += 1
        return min_length