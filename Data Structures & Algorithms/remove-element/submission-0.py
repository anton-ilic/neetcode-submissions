class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current = 0
        # count = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                # count += 1
                continue
            nums[current] = nums[i]
            current += 1
        return current