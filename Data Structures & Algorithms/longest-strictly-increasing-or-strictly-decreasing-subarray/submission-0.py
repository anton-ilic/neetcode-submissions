class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 1
        current = 1
        longer = True   # True = increasing, False = decreasing

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                current = 1

            elif nums[i] < nums[i + 1]:
                if longer:
                    current += 1
                else:
                    current = 2
                    longer = True

            else:  # nums[i] > nums[i + 1]
                if not longer:
                    current += 1
                else:
                    current = 2
                    longer = False

            longest = max(longest, current)

        return longest

            
        