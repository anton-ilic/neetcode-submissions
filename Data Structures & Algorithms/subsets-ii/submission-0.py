class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # either include it, or don't include it
        nums.sort()
        ans = []
        def backtrack(nums, i, current):
            if i >= len(nums):
                ans.append(current)
                return 

            current_copy = [i for i in current]
            current_copy.append(nums[i])
            backtrack(nums, i + 1, current_copy)
            # need to prevent [1, 1] ==> 1 ignore // ignore 1
            current_digit = nums[i]
            while i < len(nums) and nums[i] == current_digit:
                i += 1
            backtrack(nums, i, current)
        backtrack(nums, 0, [])
        return ans