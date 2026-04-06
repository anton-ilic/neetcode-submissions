class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum * 2 + num == total:
                return i
            left_sum += num

        return -1
