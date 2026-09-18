class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of 0 to len(nums + 1)
        total = sum(nums)
        length =  len(nums)
        difference = length * (length + 1) // 2
        return difference - total