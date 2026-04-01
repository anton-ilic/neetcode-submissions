class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sums = [nums[0]] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                sums[0] = nums[0]
            else:
                sums[i] = max(sums[i - 1] + sums[i], sums[i])
        
        # do prefix and suffix sums
        
        max_sum = max(sums)

        # max subarray sum
        max_sums = [None] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                max_sums[i] = nums[i]
            else:
                max_sums[i] = max(max_sums[i - 1] + nums[i], nums[i])

        max_sum = max(max_sums)

        if max_sum < 0:
            return max_sum

        # min subarray sum
        min_sums = [None] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                min_sums[i] = nums[i]
            else:
                min_sums[i] = min(min_sums[i - 1] + nums[i], nums[i])

        return max(max_sum, sum(nums) - min(min_sums))