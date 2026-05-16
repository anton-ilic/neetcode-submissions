class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_one = set(nums1)
        set_two = set(nums2)

        first = []
        second = []
        for item in set_one:
            if item not in set_two:
                first.append(item)
        
        for item in set_two:
            if item not in set_one:
                second.append(item)
        return [first, second]