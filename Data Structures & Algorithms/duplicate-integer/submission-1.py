class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # in place ==> sort then compare adjacency
        # not in place ==> seen set? 
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False