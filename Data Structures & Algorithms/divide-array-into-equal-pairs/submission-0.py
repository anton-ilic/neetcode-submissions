class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        
        for v in counts.values():
            if v % 2 != 0:
                return False
        return True