class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for i in range(0, len(nums)):
            element = nums[i]
            if elements.get(element) != None:
                return [elements.get(element), i]
            elements[target - element] = i
        return -1

