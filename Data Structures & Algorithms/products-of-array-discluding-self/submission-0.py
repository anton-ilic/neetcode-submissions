class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]

        # for i in range(len(nums) - 2, -1, -1):
        #     ans[i] = nums[ i + 1]
        low = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * low
            low = low * nums[i]
        
        return ans