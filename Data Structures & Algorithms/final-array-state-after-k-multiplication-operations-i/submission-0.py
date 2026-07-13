class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # since order needs to be preserved and k <= 10; jsut bruteforce
        for _ in range(k):
            min_value = min(nums)
            for i in range(0, len(nums)):
                if nums[i] == min_value:
                    nums[i] = nums[i] * multiplier
                    break
        return nums
