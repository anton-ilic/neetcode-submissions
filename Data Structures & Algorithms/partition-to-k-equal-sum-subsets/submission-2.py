class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # k subsets; nums must be divisible by k
        total = sum(nums) // k # there r k bins summing to nums total
        used = [False] * len(nums)
        if sum(nums) % k != 0:
            return False
        
        def backtrack(j, k, currentSum):
            if k == 0:
                return True

            if currentSum == total:
                return backtrack(0, k - 1, 0)
            
            for i in range(j, len(nums)):
                if used[i]:
                    continue
                
                if currentSum + nums[i] > total:
                    continue

                if currentSum == total:
                    return backtrack(0, k - 1, 0)
                used[i] = True
                if backtrack(i + 1, k, currentSum + nums[i]):
                    return True
                # help here? 
                used[i] = False
            
            return False
        return backtrack(0, k, 0)
        
