class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low = 0
        for i in range(0, len(nums)):
            if i == len(nums) - 1:
                nums[low] = nums[i]
                return low + 1

            if nums[i] == nums[i + 1]:
                continue
            nums[low] = nums[i]
            low += 1
        return low + 1
        