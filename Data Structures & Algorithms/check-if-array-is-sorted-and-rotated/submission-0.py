class Solution:
    def check(self, nums: List[int]) -> bool:
        # sorted in ascending then rotated ==> means every pair low < high except one
        # must be min; and high of that part must be less then 1 IF rotated
        count = 0
        for i in range(0, len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            count += 1
        
        if nums[-1] > nums[0]:
            count += 1
        return count <= 1
        