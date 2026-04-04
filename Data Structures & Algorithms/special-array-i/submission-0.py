class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for i in range(0, len(nums) - 1):
            if i == 0:
                if nums[i] % 2 == nums[i + 1] % 2:
                    return False
            else:
                if nums[i - 1] % 2 == nums[i + 1] % 2 and nums[i] % 2 != nums[i + 1] % 2:
                    pass
                else:
                    return False
        return True
            
            
            

