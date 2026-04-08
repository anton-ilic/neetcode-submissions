class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # bin numbers by 'start' 
        for i in range(0, len(nums)):
            nums[i] = str(nums[i])

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                # pairwise comparaison 
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                    nums[j], nums[i] = nums[i], nums[j]

        ans = ''.join(nums)

        if ans[0] == "0":
            return "0"
        return ans
            