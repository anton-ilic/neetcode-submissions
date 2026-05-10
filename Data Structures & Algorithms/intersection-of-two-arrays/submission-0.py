class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first = set(nums1)
        second = set(nums2)
        ans = []
        for i in first:
            if i in second:
                ans.append(i)
        return ans