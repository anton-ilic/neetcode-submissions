class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        sol = []
        end = len(nums)
        for current in range(0, end):
            if current > 0 and nums[current] == nums[current - 1]:
                continue
                
            target = -nums[current]
            low = current + 1
            high = end - 1
            while low < high:
                if nums[low] + nums[high] == target:
                    sol.append([-target, nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1

                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

                elif nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1
        return sol

                